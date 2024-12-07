# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional
from .common import SchoolCategory, Timing
from ..utils.region import Region

__all__ = [
    "SchoolCategory",
    "Timing",
    "FoundationType",
    "HighSchoolCategory",
    "HighSchoolSubtype",
    "SchoolPurpose",
    "AdmissionPeriod",
    "GenderComposition",
    "SchoolInfo",
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class FoundationType(Enum):
    """
    학교 설립 구분 열거형입니다.
    """
    PUBLIC      = "PUBLIC"
    """공립 학교입니다."""
    PRIVATE     = "PRIVATE"
    """사립 학교입니다."""
    NATIONAL    = "NATIONAL"
    """국립 학교입니다."""
    OTHERS      = "OTHERS"
    """기타 설립 학교입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class HighSchoolCategory(Enum):
    """
    고등학교 일반, 전문 구분 열거형입니다.
    """
    NORMAL     = "NORMAL"
    """일반계 고등학교입니다."""
    VOCATIONAL = "VOCATIONAL"
    """전문계 고등학교입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class HighSchoolSubtype(Enum):
    """
    고등학교 계열 열거형입니다.
    """
    NORMAL          = "NORMAL"
    """일반 고등학교입니다."""
    SPECIALIZED     = "SPECIALIZED"
    """특성화 고등학교입니다."""
    SPECIAL_PURPOSE = "SPECIAL_PURPOSE"
    """특수 목적 고등학교입니다."""
    AUTONOMOUS      = "AUTONOMOUS"
    """자율형 고등학교입니다."""
    OTHERS          = "OTHERS"
    """기타 고등학교입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class SchoolPurpose(Enum):
    """
    특수 목적 고등학교 계열 열거형입니다.
    """
    INTERNATIONAL = "INTERNATIONAL"
    """국제 계열 특수 목적 고등학교입니다."""
    PHYSICAL      = "PHYSICAL"
    """체육 계열 특수 목적 고등학교입니다."""
    ART           = "ART"
    """예술 계열 특수 목적 고등학교입니다."""
    SCIENCE       = "SCIENCE"
    """과학 계열 특수 목적 고등학교입니다."""
    LANGUAGE      = "LANGUAGE"
    """외국어 계열 특수 목적 고등학교입니다."""
    INDUSTRY      = "INDUSTRY"
    """산업 수요 맞춤형 특수 목적 고등학교입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class AdmissionPeriod(Enum):
    """
    입시 전기, 후기 구분 열거형입니다.
    """
    EARLY = "EARLY"
    """전기 입시 유형입니다."""
    LATE  = "LATE"
    """후기 입시 유형입니다."""
    BOTH  = "BOTH"
    """전후기 입시 유형입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class GenderComposition(Enum):
    """
    단성, 혼성 구분 열거형입니다.
    """
    MIXED      = "MIXED"
    """혼성 학교입니다."""
    BOYS_ONLY  = "BOYS_ONLY"
    """남자 단성 학교입니다."""
    GIRLS_ONLY = "GIRLS_ONLY"
    """여자 단성 학교입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class SchoolInfo:
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
    school_category: SchoolCategory
    """학교 종류명"""
    jurisdiction_name: str
    """관할 조직명"""
    foundation_type: FoundationType
    """설립명"""
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
    gender_composition: GenderComposition
    """남녀공학 구분명"""
    fax_number: Optional[str]
    """팩스 번호"""
    subtype: Optional[HighSchoolSubtype]
    """고등학교 구분명"""
    industry_supports: bool
    """산업체 특별 학급 존재 여부"""
    high_school_category: Optional[HighSchoolCategory]
    """고등학교 일반 전문 구분명"""
    purpose: Optional[SchoolPurpose]
    """특수 목적 고등학교 계열명"""
    admission_period: AdmissionPeriod
    """입시 전후기 구분명"""
    timing: Timing
    """주야 구분명"""
    founded_date: date
    """설립 일자"""
    anniversary: date
    """개교 기념일"""
