# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .common import CourseType, Timing

__all__ = ["CourseType", "Timing", "Classroom"]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Classroom:
    """
    학급 정보를 나타내는 데이터 클래스입니다.
    """

    year: int
    """학년도"""
    grade: int
    """학년"""
    timing: Optional[Timing]
    """주야과정명"""
    course: CourseType
    """학교과정명"""
    department: Optional[str]
    """계열명"""
    major: Optional[str]
    """학과명"""
    name: Optional[str]
    """학급명"""
