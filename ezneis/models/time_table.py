# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional
from .common import Timing

__all__ = [
    "Timing",
    "Timetable"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Timetable:
    semester: int
    """학기"""
    date: date
    """시간표 일자"""
    timing: Optional[Timing]
    """주야 과정명"""
    department: Optional[str]
    """계열명"""
    major: Optional[str]
    """학과명"""
    grade: int
    """학년"""
    lecture_room_name: Optional[str]
    """강의실명"""
    classroom_name: str
    """학급명"""
    period: int
    """교시"""
    subject: str
    """수업 내용"""
