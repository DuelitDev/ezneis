# -*- coding: utf-8 -*-
from datetime import datetime

from ..models.time_table import *
from .common import Parser

__all__ = ["TimetableParser"]


class TimetableParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Timetable:
        grade = int(data["GRADE"])
        semester = int(data["SEM"])
        date = datetime.strptime(data["ALL_TI_YMD"], "%Y%m%d").date()
        period = int(data["PERIO"])
        subject = data["ITRT_CNTNT"]
        classroom_name = data["CLASS_NM"]
        if "DGHT_SC_NM" in data:
            match data["DGHT_SC_NM"]:
                case "주간":
                    timing = Timing.DAY
                case "야간":
                    timing = Timing.NIGHT
                case _:
                    timing = None
        else:
            timing = None
        lecture_room_name = data["CLRM_NM"] if "CLRM_NM" in data else None
        major = data["DDDEP_NM"] if "DDDEP_NM" in data else None
        department = data["ORD_SC_NM"] if "ORD_SC_NM" in data else None
        return Timetable(
            grade=grade,
            semester=semester,
            date=date,
            period=period,
            subject=subject,
            classroom_name=classroom_name,
            timing=timing,
            lecture_room_name=lecture_room_name,
            major=major,
            department=department,
        )
