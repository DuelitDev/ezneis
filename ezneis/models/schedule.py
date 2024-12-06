# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional, SupportsIndex
from .common import Timing

__all__ = [
    "ScheduleCategory",
    "Timing",
    "GradeCorrespondence",
    "Schedule"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class ScheduleCategory(Enum):
    """
    행사 유형 열거형입니다.
    """
    DAY_OFF = "DAY_OFF"
    """휴업일입니다."""
    HOLIDAY = "HOLIDAY"
    """공휴일입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class GradeCorrespondence:
    """
    행사에 해당하는 학년을 나타내는 데이터 클래스입니다.
    """
    grade0: bool
    """0학년의 행사 해당 여부입니다."""
    grade1: bool
    """1학년의 행사 해당 여부입니다."""
    grade2: bool
    """2학년의 행사 해당 여부입니다."""
    grade3: bool
    """3학년의 행사 해당 여부입니다."""
    grade4: bool
    """4학년의 행사 해당 여부입니다."""
    grade5: bool
    """5학년의 행사 해당 여부입니다."""
    grade6: bool
    """6학년의 행사 해당 여부입니다."""
    grade7: bool
    """7학년의 행사 해당 여부입니다."""

    def __getitem__(self, indices: slice | SupportsIndex) -> tuple[bool, ...]:
        return (self.grade0, self.grade1, self.grade2, self.grade3,
                self.grade4, self.grade5, self.grade6, self.grade7)[indices]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Schedule:
    """
    학사 일정을 나타내는 데이터 클래스입니다.
    """
    year: int
    """학년도"""
    time: Optional[Timing]
    """주야 과정명"""
    category: Optional[ScheduleCategory]
    """행사 유형 (수업 공제일명)"""
    date: date
    """학사 일자"""
    name: str
    """행사명"""
    description: Optional[str]
    """행사 내용"""
    correspondence: GradeCorrespondence
    """학년 행사 여부"""
