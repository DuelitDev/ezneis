# -*- coding: utf-8 -*-
from datetime import datetime
from .common import Parser
from ..models.time_table import *

__all__ = [
    "TimetableParser"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class TimetableParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Timetable:
        grade          = int(data["GRADE"])
        semester       = int(data["SEM"])
        date           = datetime.strptime(data["ALL_TI_YMD"],
                                           "%Y%m%d").date()
        period         = int(data["PERIO"])
        subject        = data["ITRT_CNTNT"]
        classroom_name = data["CLASS_NM"]
        if "DGHT_SC_NM" in data:
            match data["DGHT_SC_NM"]:
                case "주간": timing = Timing.DAY
                case "야간": timing = Timing.NIGHT
                case _:      timing = None
        else:
            timing = None
        lecture_room_name = data["CLRM_NM"] if "CLRM_NM" in data else None
        major             = data["DDDEP_NM"] if "DDDEP_NM" in data else None
        if "ORD_SC_NM" in data:
            match data["ORD_SC_NM"]:
                case "일반계":     department = Department.NORMAL
                case "전문계":     department = Department.VOCATIONAL
                case "특성화":     department = Department.SPECIALIZED
                case "국제계":     department = Department.INTERNATIONAL
                case ("가사실업계열" |
                      "가사실업계" |
                      "가사계"):   department = Department.BUSINESS
                case ("전자미디어계" |
                      "상업정보계열" |
                      "상업계" |
                      "직업"):     department = Department.COMMERCE
                case ("공업계열" |
                      "공업계"):   department = Department.TECHNICAL
                case ("도시형첨단농업경영계열" |
                      "농생명산업계열" |
                      "농생명계" |
                      "농업계"):   department = Department.AGRICULTURE
                case "수산해양계": department = Department.FISHERIES
                case "통합계":     department = Department.INTEGRATED
                case "외국어계":   department = Department.LANGUAGE
                case "과학계":     department = Department.SCIENCE
                case "체육계":     department = Department.PHYSICAL
                case "예술계":     department = Department.ART
                case "대안":       department = Department.ALTERNATIVE
                case "공동실습소": department = Department.TRAINING
                case _:            department = None
        else:
            department = None
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
