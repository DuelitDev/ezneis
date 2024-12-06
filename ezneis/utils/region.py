# -*- coding: utf-8 -*-
from enum import Enum

__all__ = [
    "Region"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class Region(Enum):
    """
    시도교육청코드 열거형입니다.
    """
    SEOUL = "B10"
    """서울특별시의 시도교육청코드 "B10"입니다."""
    BUSAN = "C10"
    """부산광역시의 시도교육청코드 "C10"입니다."""
    DAEGU = "D10"
    """대구광역시의 시도교육청코드 "D10"입니다."""
    INCHEON = "E10"
    """인천광역시의 시도교육청코드 "E10"입니다."""
    GWANGJU = "F10"
    """광주광역시의 시도교육청코드 "F10"입니다."""
    DAEJEON = "G10"
    """대전광역시의 시도교육청코드 "G10"입니다."""
    ULSAN = "H10"
    """울산광역시의 시도교육청코드 "H10"입니다."""
    SEJONG = "I10"
    """세종특별자치시의 시도교육청코드 "I10"입니다."""
    GYEONGGI = "J10"
    """경기도의 시도교육청코드 "J10"입니다."""
    GANGWON = "K10"
    """강원특별자치도의 시도교육청코드 "K10"입니다."""
    CHUNGBUK = "M10"
    """충청북도의 시도교육청코드 "M10"입니다."""
    CHUNGNAM = "N10"
    """충청남도의 시도교육청코드 "N10"입니다."""
    JEONBUK = "P10"
    """전북특별자치도의 시도교육청코드 "P10"입니다."""
    JEONNAM = "Q10"
    """전라남도의 시도교육청코드 "Q10"입니다."""
    GYEONGBUK = "R10"
    """경상북도의 시도교육청코드 "R10"입니다."""
    GYEONGNAM = "S10"
    """경상남도의 시도교육청코드 "S10"입니다."""
    JEJU = "T10"
    """제주특별자치도의 시도교육청코드 "T10"입니다."""
    FOREIGNER = "V10"
    """재외 한국 학교의 시도교육청코드 "V10"입니다."""
