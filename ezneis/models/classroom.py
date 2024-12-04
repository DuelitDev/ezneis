# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from .common import Timing

__all__ = [
    "Timing",
    "CourseType",
    "Classroom",
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class CourseType(Enum):
    """
    학교 과정의 유형을 나타내는 열거형입니다.
    """
    PRESCHOOL  = "PRESCHOOL"
    """유치원 과정입니다."""
    ELEMENTARY = "ELEMENTARY"
    """초등학교 과정입니다."""
    MIDDLE     = "MIDDLE"
    """중학교 과정입니다."""
    HIGH       = "HIGH"
    """고등학교 과정입니다."""
    SPECIALITY = "SPECIALITY"
    """특수학교 과정입니다."""


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
    name: Optional[str]
    """학급명"""
    major: Optional[str]
    """학과명"""
    course: CourseType
    """학교과정명"""
    department: Optional[str]
    """계열명"""
    timing: Optional[Timing]
    """주야과정명"""
