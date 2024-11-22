# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional
from .common import Timing, Department

__all__ = [
    "Timing",
    "Department",
    "Timetable",
]


@dataclass(frozen=True)
class Timetable:
    grade: int
    semester: int
    date: date
    period: int
    subject: str
    class_name: str
    timing: Optional[Timing] = None
    room_name: Optional[str] = None
    major: Optional[str] = None
    department: Optional[Department] = None
