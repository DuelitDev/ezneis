# -*- coding: utf-8 -*-
"""
학교 기본 정보 모듈

이 모듈은 NEIS Open API를 통해 학교 기본 정보를 조회하는 기능을 제공합니다.
SchoolInfo 클래스는 학교 기본 정보를 나타내는 데이터 클래스이며,
SchoolInfoBuilder 클래스는 학교 정보 조회를 위한 쿼리를 구성하는 빌더 클래스입니다.

**사용례**::

    from ezneis import SyncSession
    from ezneis.models import SchoolInfoBuilder
    from ezneis.region import Region

    # 동기 세션 생성
    session = SyncSession("API_KEY")

    # 빌더를 사용하여 쿼리 구성
    builder = SchoolInfoBuilder().region(Region.SEOUL).name("서울고등학교")

    # 데이터 조회
    schools = builder >> session

    # 결과 출력
    for school in schools:
        print(f"학교명: {school.name}")
        print(f"주소: {school.address}")
        print(f"전화번호: {school.tel_number}")
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from .core import CoreModel, CoreBuilder
from ..http import Service
from ..region import Region

__all__ = [
    "SchoolInfo",
    "SchoolInfoBuilder",
]


@dataclass(frozen=True)
class SchoolInfo(CoreModel):
    """
    학교 기본 정보를 나타내는 데이터 클래스입니다.

    이 클래스는 NEIS Open API에서 제공하는 학교 기본 정보를 담고 있습니다.
    학교의 이름, 주소, 전화번호 등 기본적인 정보를 포함합니다.

    :ivar region: 시도 교육청 코드
    :vartype region: Region
    :ivar code: 행정 표준 코드
    :vartype code: str
    :ivar name: 학교명
    :vartype name: str
    :ivar english_name: 영문 학교명
    :vartype english_name: str 또는 None
    :ivar zip_code: 도로명 우편 번호
    :vartype zip_code: int 또는 None
    :ivar address: 도로명 주소
    :vartype address: str 또는 None
    :ivar address_detail: 도로명 상세 주소
    :vartype address_detail: str 또는 None
    :ivar tel_number: 전화 번호
    :vartype tel_number: str
    :ivar website: 홈페이지 주소
    :vartype website: str 또는 None
    :ivar fax_number: 팩스 번호
    :vartype fax_number: str 또는 None
    :ivar founded_date: 설립 일자
    :vartype founded_date: date
    :ivar anniversary: 개교 기념일
    :vartype anniversary: date
    """

    region: Region
    """시도 교육청 코드"""
    code: str
    """행정 표준 코드"""
    name: str
    """학교명"""
    english_name: str | None
    """영문 학교명"""
    zip_code: int | None
    """도로명 우편 번호"""
    address: str | None
    """도로명 주소"""
    address_detail: str | None
    """도로명 상세 주소"""
    tel_number: str
    """전화 번호"""
    website: str | None
    """홈페이지 주소"""
    fax_number: str | None
    """팩스 번호"""
    founded_date: date
    """설립 일자"""
    anniversary: date
    """개교 기념일"""

    @classmethod
    def from_dict(cls, data: dict) -> SchoolInfo:
        """
        API 응답 데이터로부터 SchoolInfo 객체를 생성합니다.

        :param data: NEIS Open API의 응답 데이터
        :type data: dict
        :return: 생성된 SchoolInfo 객체
        :rtype: SchoolInfo
        """
        # 시도 교육청 코드
        region = Region(data["ATPT_OFCDC_SC_CODE"])
        # 행정 표준 코드
        code = data["SD_SCHUL_CODE"]
        # 학교명
        name = data["SCHUL_NM"]
        # 영문 학교명
        english_name = data["ENG_SCHUL_NM"]
        # 도로명 우편 번호
        zip_code = int(zc) if (zc := data["ORG_RDNZC"]) is not None else None
        # 도로명 주소
        address = data["ORG_RDNMA"]
        # 도로명 상세 주소
        address_detail = data["ORG_RDNDA"]
        # 전화 번호
        tel_number = data["ORG_TELNO"]
        # 홈페이지 주소
        website = data["HMPG_ADRES"]
        # 팩스 번호
        fax_number = data["ORG_FAXNO"]
        # 설립 일자
        founded_date = datetime.strptime(data["FOND_YMD"], "%Y%m%d").date()
        # 개교 기념일
        anniversary = datetime.strptime(data["FOAS_MEMRD"], "%Y%m%d").date()
        return cls(
            region=region,
            code=code,
            name=name,
            english_name=english_name,
            zip_code=zip_code,
            address=address,
            address_detail=address_detail,
            tel_number=tel_number,
            website=website,
            fax_number=fax_number,
            founded_date=founded_date,
            anniversary=anniversary,
        )


class SchoolInfoBuilder(CoreBuilder):
    """
    학교 기본 정보 조회를 위한 빌더 클래스입니다.

    이 클래스는 NEIS Open API의 학교 기본 정보 서비스에 대한 쿼리를 구성하는 데 사용됩니다.
    메서드 체이닝을 통해 쿼리 파라미터를 설정하고, 연산자 오버로딩(>>)을 통해 데이터를 조회할 수 있습니다.

    **사용례**::

        # 서울특별시의 "서울고등학교" 정보 조회
        sess = SyncSession("your_api_key")
        req = SchoolInfoBuilder().region(Region.SEOUL).name("서울고등학교") >> sess
        schools = req
    """
    @property
    def _service(self) -> Service:
        """
        사용할 NEIS Open API 서비스를 반환합니다.

        :return: 학교 기본 정보 서비스(SCHOOL_INFO)
        :rtype: Service
        """
        return Service.SCHOOL_INFO

    @property
    def _model(self) -> type[CoreModel]:
        """
        API 응답을 변환할 모델 클래스를 반환합니다.

        :return: SchoolInfo 클래스
        :rtype: type[CoreModel]
        """
        return SchoolInfo

    def __rrshift__(self, other) -> SchoolInfoBuilder:
        """
        다른 빌더나 모델로부터 파라미터를 상속받습니다.

        이 메서드는 << 연산자를 통해 호출됩니다.

        :param other: 파라미터를 상속받을 빌더 또는 모델
        :type other: Any
        :return: 파라미터가 업데이트된 빌더 인스턴스
        :rtype: SchoolInfoBuilder
        """
        # TODO: 다른 빌더 또는 모델로부터 파라미터 상속 구현
        return self

    def region(self, region: Region) -> SchoolInfoBuilder:
        """
        시도 교육청 코드를 설정합니다.

        :param region: 조회할 시도 교육청 코드
        :type region: Region
        :return: 메서드 체이닝을 위한 빌더 인스턴스
        :rtype: SchoolInfoBuilder

        **사용례**::

            # 서울특별시 교육청 코드 설정
            builder = SchoolInfoBuilder().region(Region.SEOUL)
        """
        self._param["ATPT_OFCDC_SC_CODE"] = region.value
        return self

    def code(self, code: str) -> SchoolInfoBuilder:
        """
        학교 행정 표준 코드를 설정합니다.

        :param code: 조회할 학교의 행정 표준 코드
        :type code: str
        :return: 메서드 체이닝을 위한 빌더 인스턴스
        :rtype: SchoolInfoBuilder

        **사용례**::

            # 특정 학교 코드 설정
            builder = SchoolInfoBuilder().code("7010569")
        """
        self._param["SD_SCHUL_CODE"] = code
        return self

    def name(self, name: str) -> SchoolInfoBuilder:
        """
        학교명을 설정합니다.

        :param name: 조회할 학교명
        :type name: str
        :return: 메서드 체이닝을 위한 빌더 인스턴스
        :rtype: SchoolInfoBuilder

        **사용례**::

            # 학교명으로 검색
            builder = SchoolInfoBuilder().name("서울고등학교")
        """
        self._param["SCHUL_NM"] = name
        return self
