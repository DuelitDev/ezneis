# -*- coding: utf-8 -*-
from dataclasses import dataclass
from .common import Timing

__all__ = [
    "Timing",
    "Department"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Department:
    """
    학과 계열 정보를 나타내는 데이터 클래스입니다.
    """
    name: str
    """계열명"""
    timing: Timing
    """주야과정명"""
    is_special_industry_timing: bool
    """산업체특별 주야과정 여부"""
