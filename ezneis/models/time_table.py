# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional
from .common import Timing

__all__ = [
    "Timing",
    "Timetable",
]


@dataclass(frozen=True)
class Timetable:
    grade: int
    semester: int
    date: date
    period: int
    subject: str
    classroom_name: str
    timing: Optional[Timing] = None
    lecture_room_name: Optional[str] = None
    major: Optional[str] = None
    department: Optional[str] = None
