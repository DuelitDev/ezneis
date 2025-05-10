# -*- coding: utf-8 -*-
from __future__ import annotations
from .common import Services
from ..exceptions import (
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

        from ezneis.http import SyncSession
        from ezneis.http.common import Services

        API_KEY = "your_api_key"
        # API 키를 사용하여 세션 생성
        sess = SyncSession(API_KEY)

        # 컨텍스트 매니저를 이용하여 세션 생성
        with SyncSession(API_KEY) as sess:
           data = sess.get(Services.SCHOOL_INFO, limit=10)
    """

    def __init__(self, key: str):
        """
        SyncSession 인스턴스를 초기화합니다.

        :param key: 나이스 교육정보 OPEN API 인증 키
        :type key: str
        """
        self._key = key
        self._max_req = 5 if not key else 1000
        self._session = requests.Session()
        self._closed = False

    def __del__(self):
        """
        인스턴스가 가비지 컬렉션될 때 세션을 닫습니다.
        """
        self.close()

    def __enter__(self) -> SyncSession:
        """
        컨텍스트 매니저 진입 메서드입니다.

        :return: 현재 세션 인스턴스
        :rtype: SyncSession
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        컨텍스트 매니저 종료 메서드입니다. 세션을 자동으로 닫습니다.

        :param exc_type: 예외 타입
        :param exc_val: 예외 값
        :param exc_tb: 예외 트레이스백
        """
        self.close()

    @property
    def closed(self) -> bool:
        """
        세션이 닫혔는지 여부를 반환합니다.

        :return: 세션이 닫혔으면 True, 그렇지 않으면 False
        :rtype: bool
        """
        return self._closed

    def get(self, svc: Services, *, limit: int | None, **kwargs) -> list[dict]:
        """
        나이스 교육정보 OPEN API에서 데이터를 조회합니다.

        이 메서드는 지정된 서비스에서 데이터를 가져오며, 필요한 경우 여러 페이지에 걸쳐 데이터를 수집합니다.

        :param svc: 조회할 서비스 (Services 열거형)
        :type svc: Services
        :param limit: 가져올 최대 레코드 수 (None인 경우 모든 레코드 조회)
        :type limit: int 또는 None
        :param kwargs: 서비스별 추가 매개변수
        :return: 조회된 데이터 레코드 목록
        :rtype: list[dict]
        :raises SessionClosedException: 세션이 이미 닫힌 경우
        :raises ServiceUnavailableError: 서비스 요청에 실패한 경우
        :raises InternalServiceError: 서비스 내부 오류가 발생한 경우

        **사용례**::

            session = SyncSession("your_api_key")

            # 학교 정보 조회
            schools = session.get(
                Services.SCHOOL_INFO,
                limit=None,                # 모든 데이터 조회
                ATPT_OFCDC_SC_CODE="B10",  # 서울특별시교육청
                SCHUL_KND_SC_NM="고등학교"   # 학교 종류
            )

            # 급식 정보 조회
            meals = session.get(
                Services.MEALS,
                limit=10,                  # 10개 데이터 조회
                ATPT_OFCDC_SC_CODE="J10",  # 경기도교육청
                SD_SCHUL_CODE="1234567",   # 학교 코드
                MLSV_YMD="202505"          # 급식 제공 년월
            )

            # 결과 처리
            for school in schools:
                print(f"학교명: {school['SCHUL_NM']}")
        """
        if self.closed:
            raise SessionClosedException
        params = {
            **kwargs,
            "KEY": self._key,
            "Type": "json",
            "pIndex": 1,
            "pSize": (limit if limit and limit <= self._max_req else self._max_req),
        }
        # TODO: concurrent.futures를 이용한 병렬 IO 처리
        records = []
        expected = limit  # 가져와야 할 총 레코드 수 (None일 경우 전체 요청)
        # expected 수만큼 데이터를 모두 가져올 때까지 반복
        while expected is None or expected - len(records) > 0:
            response = self._session.get(svc.url, params=params)
            if response.status_code != 200:
                raise ServiceUnavailableError(svc.url)
            payload = orjson.loads(response.content)
            # 서비스 데이터가 누락된 경우 예외 처리
            if svc.value not in payload:
                code = payload["RESULT"]["CODE"]
                if code == InternalServiceCode.NOT_FOUND.value:
                    break
                message = payload["RESULT"]["MESSAGE"]
                raise InternalServiceError(code, message)
            # 응답 데이터에서 헤더와 행 추출
            header, body = payload[svc.value]
            records.extend(body["row"])
            # limit이 지정되지 않은 경우 expected를 전체 레코드 수로 설정
            if expected is None:
                expected = header["head"][0]["list_total_count"]
            # 다음 페이지로 이동
            params["pIndex"] += 1
        return records

    def close(self):
        """
        세션을 닫고 관련 리소스를 해제합니다.

        이 메서드는 세션과 관련된 모든 리소스를 정리하고 세션을 닫습니다.
        세션이 이미 닫혀 있는 경우에도 안전하게 호출할 수 있습니다.
        """
        if self._session:
            self._session.close()
            self._closed = True
