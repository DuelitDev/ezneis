# -*- coding: utf-8 -*-
from datetime import datetime
from .common import Parser
from ..models.schedule import *

__all__ = [
    "SchoolScheduleParser"
]


class SchoolScheduleParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> SchoolSchedule:
        year = int(data["AY"])
        name = data["EVENT_NM"]
        description = data["EVENT_CNTNT"]
        match data["DGHT_CRSE_SC_NM"]:
            case "주간": time = ScheduleTime.DAY
            case "야간": time = ScheduleTime.NIGHT
            case _:     time = None
        correspondence = GradeCorrespondence(
            grade0=False,
            grade1=data["ONE_GRADE_EVENT_YN"]   == 'Y',
            grade2=data["TW_GRADE_EVENT_YN"]    == 'Y',
            grade3=data["THREE_GRADE_EVENT_YN"] == 'Y',
            grade4=data["FR_GRADE_EVENT_YN"]    == 'Y',
            grade5=data["FIV_GRADE_EVENT_YN"]   == 'Y',
            grade6=data["SIX_GRADE_EVENT_YN"]   == 'Y',
            grade7=False
        )
        match data["SBTR_DD_SC_NM"]:
            case "휴업일": category = ScheduleCategory.DAY_OFF
            case "공휴일": category = ScheduleCategory.HOLIDAY
            case _:       category = None
        date = datetime.strptime(data["AA_YMD"], "%Y%m%d").date()
        return SchoolSchedule(
            year=year,
            name=name,
            description=description,
            time=time,
            correspondence=correspondence,
            category=category,
            date=date,
        )
