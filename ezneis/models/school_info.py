# -*- coding: utf-8 -*-
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional, Sequence
from .common import CoreModel, CoreBuilder
from ..http import AsyncSession, SyncSession, Services
from ..region import Region

__all__ = [
    "SchoolInfo",
    "SchoolInfoBuilder",
]


@dataclass(frozen=True)
class SchoolInfo(CoreModel):
    """
    학교 기본 정보를 나타내는 데이터 클래스입니다.
    """

    region: Region
    """시도 교육청 코드"""
    code: str
    """행정 표준 코드"""
    name: str
    """학교명"""
    english_name: Optional[str]
    """영문 학교명"""
    zip_code: Optional[str]
    """도로명 우편 번호"""
    address: Optional[str]
    """도로명 주소"""
    address_detail: Optional[str]
    """도로명 상세 주소"""
    tel_number: str
    """전화 번호"""
    website: Optional[str]
    """홈페이지 주소"""
    fax_number: Optional[str]
    """팩스 번호"""
    founded_date: date
    """설립 일자"""
    anniversary: date
    """개교 기념일"""

    @classmethod
    def from_dict(cls, data: dict) -> SchoolInfo:
        # 시도 교육청 코드
        region = Region(data["ATPT_OFCDC_SC_CODE"])
        # 행정 표준 코드
        code = data["SD_SCHUL_CODE"]
        # 학교명
        name = data["SCHUL_NM"]
        # 영문 학교명
        english_name = data["ENG_SCHUL_NM"]
        # 도로명 우편 번호
        zip_code = zc if (zc := data["ORG_RDNZC"]) is not None else None
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
    def region(self, region: Region) -> SchoolInfoBuilder:
        self._param["ATPT_OFCDC_SC_CODE"] = region.value
        return self
    
    def code(self, code: str) -> SchoolInfoBuilder:
        self._param["SD_SCHUL_CODE"] = code
        return self
    
    def name(self, name: str) -> SchoolInfoBuilder:
        self._param["SCHUL_NM"] = name
        return self
    
    def fetch_sync(self, sess: SyncSession) -> Sequence[SchoolInfo]:
        return tuple(
            SchoolInfo.from_dict(data)
            for data in sess.get(Services.SCHOOL_INFO, **self._param)
        )

    async def fetch_async(self, sess: AsyncSession) -> Sequence[SchoolInfo]:
        return tuple(
            SchoolInfo.from_dict(data)
            for data in await sess.get(Services.SCHOOL_INFO, **self._param)
        )
