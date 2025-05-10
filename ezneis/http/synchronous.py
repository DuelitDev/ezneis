# -*- coding: utf-8 -*-
from __future__ import annotations
from concurrent import futures
from .service import Service
from ..exceptions import (
    DataNotFoundException,
    InternalServiceCode,
    InternalServiceError,
    ServiceUnavailableError,
    SessionClosedException,
)
import requests
import orjson

__all__ = [
    "SyncSession",
]


class SyncSession:
    """
    나이스 교육정보 OPEN API에 접근하기 위한 동기식 HTTP 세션을 제공합니다.

    **사용례**::

        from ezneis.http import SyncSession, Service


        key = "your_api_key"
        # API 키를 사용하여 세션 생성
        sess = SyncSession(key)

        # 컨텍스트 매니저를 이용하여 세션 생성
        with SyncSession(key) as sess:
           data = sess.get(Service.SCHOOL_INFO, expected=10)
    """

    def __init__(self, key: str):
        """
        SyncSession 인스턴스를 초기화합니다.

        :param key: 나이스 교육정보 OPEN API 인증 키
        :type key: str
        """
        self._key = key
        self._max_req = 5 if not key else 1000
        self._session: requests.Session | None = None
        self._closed = False

    def __enter__(self) -> SyncSession:
        """
        컨텍스트 매니저 진입 메서드입니다.

        :return: 현재 세션 인스턴스
        :rtype: SyncSession
        :raises SessionClosedException: 세션이 이미 닫힌 경우
        """
        if self._closed:
            raise SessionClosedException
        self._session = requests.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        컨텍스트 매니저 종료 메서드입니다. 세션을 자동으로 닫습니다.

        :param exc_type: 예외 타입
        :param exc_val: 예외 값
        :param exc_tb: 예외 트레이스백
        """
        self.close()

    def get(self, svc: Service, *, expected: int | None = None, **kwargs) -> list[dict]:
        """
        나이스 교육정보 OPEN API에서 데이터를 조회합니다.

        이 메서드는 지정된 서비스에서 데이터를 가져오며, 필요한 경우 여러 페이지에 걸쳐 데이터를 수집합니다.

        :param svc: 조회할 서비스 (Service 열거형)
        :type svc: Service
        :param expected: 가져올 최대 레코드 수 (None인 경우 모든 레코드 조회)
        :type expected: int 또는 None
        :param kwargs: 서비스별 추가 매개변수
        :return: 조회된 데이터 레코드 목록
        :rtype: list[dict]
        :raises DataNotFoundException: 요청한 데이터를 찾을 수 없는 경우
        :raises InternalServiceError: 서비스 내부 오류가 발생한 경우
        :raises ServiceUnavailableError: 서비스 요청에 실패한 경우
        :raises SessionClosedException: 세션이 이미 닫힌 경우

        **사용례**::

            with SyncSession("your_api_key") as sess:
                # 학교 정보 조회
                schools = sess.get(
                    Service.SCHOOL_INFO,
                    expected=None,             # 모든 데이터 조회
                    ATPT_OFCDC_SC_CODE="B10",  # 서울특별시교육청
                    SCHUL_KND_SC_NM="고등학교"   # 학교 종류
                )

                # 급식 정보 조회
                meals = sess.get(
                    Service.MEALS,
                    expected=10,               # 10개 데이터 조회
                    ATPT_OFCDC_SC_CODE="J10",  # 경기도교육청
                    SD_SCHUL_CODE="1234567",   # 학교 코드
                    MLSV_YMD="202505"          # 급식 제공 년월
                )

            # 결과 처리
            for school in schools:
                print(f"학교명: {school['SCHUL_NM']}")
        """
        # 세션 상태 체크
        if self._closed:
            raise SessionClosedException
        if self._session is None:
            self._session = requests.Session()

        # 요청 작업 생성
        tasks = []
        records = []

        with futures.ThreadPoolExecutor() as executor:
            # 예상 레코드 수가 설정된 경우
            if expected is not None:
                pages = (expected + self._max_req - 1) // self._max_req
                size = min(self._max_req, expected)
                start = 1
            # 예상 레코드 수가 설정되지 않은 경우
            else:
                # 단일 요청을 통해 총 레코드 개수를 가져오기
                expected, rows = self._request(svc, 1, self._max_req, **kwargs)
                records.extend(rows)
                # 첫번째 요청을 기반으로 페이지 계산
                pages = (expected + self._max_req - 1) // self._max_req
                size = self._max_req
                start = 2
            # 페이지 갯수에 맞춰 요청 작업 생성
            for i in range(start, pages + 1):
                tasks.append(executor.submit(self._request, svc, i, size, **kwargs))

            # 병렬 요청 결과 처리
            for future in futures.as_completed(tasks):
                try:
                    result = future.result()
                    _, rows = result
                    records.extend(rows)
                # 데이터가 없는 경우는 무시
                except DataNotFoundException:
                    continue
                # 그 외 예외는 재전파
                except Exception as e:
                    raise e

            # 레코드가 없는 경우 예외 발생
            if len(records) == 0:
                raise DataNotFoundException(svc.url, kwargs)
            # 레코드를 최대 expected만큼 반환
            return records[:expected]

    def _request(
        self, svc: Service, index: int, size: int, **kwargs
    ) -> tuple[int, list[dict]]:
        """
        나이스 교육정보 OPEN API에 단일 페이지 요청을 수행합니다.

        :param svc: 요청할 서비스 (Service 열거형)
        :type svc: Service
        :param index: 요청할 페이지 번호
        :type index: int
        :param size: 페이지당 레코드 수
        :type size: int
        :param kwargs: 서비스별 추가 매개변수
        :return: (전체 레코드 수, 현재 페이지 레코드 목록) 튜플
        :rtype: tuple[int, list[dict]]
        :raises DataNotFoundException: 요청한 데이터를 찾을 수 없는 경우
        :raises InternalServiceError: 서비스 내부 오류가 발생한 경우
        :raises ServiceUnavailableError: 서비스 요청에 실패한 경우
        :raises SessionClosedException: 세션이 닫힌 경우
        """
        # 세션 상태 체크
        if not self._session or self._closed:
            raise SessionClosedException

        # 쿼리 생성
        query = {
            **kwargs,
            "KEY": self._key,
            "Type": "json",
            "pIndex": index,
            "pSize": size,
        }

        # 서비스에 쿼리 요청 후 결과 처리
        with self._session.get(svc.url, params=query) as resp:
            if resp.status_code != 200:
                raise ServiceUnavailableError(svc.url)
            payload = orjson.loads(resp.content)

        # 서비스 데이터가 누락된 경우 예외 처리
        if svc.value not in payload:
            code = payload["RESULT"]["CODE"]
            if code == InternalServiceCode.NOT_FOUND.value:
                raise DataNotFoundException(svc.url, query)
            msg = payload["RESULT"]["MESSAGE"]
            raise InternalServiceError(code, msg)

        # 응답 서비스 데이터 반환
        header, body = payload[svc.value]
        return header["head"][0]["list_total_count"], body["row"]

    def close(self):
        """
        세션을 닫고 관련 리소스를 해제합니다.

        이 메서드는 세션과 관련된 모든 리소스를 정리하고 세션을 닫습니다.
        세션이 이미 닫혀 있는 경우에도 안전하게 호출할 수 있습니다.
        """
        if self._session and not self._closed:
            self._session.close()
        self._closed = True

    @property
    def closed(self) -> bool:
        """
        세션이 닫혔는지 여부를 반환합니다.

        :return: 세션이 닫혔으면 True, 그렇지 않으면 False
        :rtype: bool
        """
        return self._closed
