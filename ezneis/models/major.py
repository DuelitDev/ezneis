# -*- coding: utf-8 -*-
from dataclasses import dataclass
from .common import Timing

__all__ = [
    "Timing",
    "Major"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Major:
    """
    학교 학과 정보를 나타내는 데이터 클래스입니다.
    """
    timing: Timing
    """주야 과정명"""
    department: str
    """계열명"""
    name: str
    """학과명"""
