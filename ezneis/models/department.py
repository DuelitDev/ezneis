# -*- coding: utf-8 -*-
from dataclasses import dataclass

from .common import Timing

__all__ = ["Timing", "Department"]


@dataclass(frozen=True)
class Department:
    """
    학과 계열 정보를 나타내는 데이터 클래스입니다.
    """

    timing: Timing
    """주야과정명"""
    name: str
    """계열명"""
