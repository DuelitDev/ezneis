# -*- coding: utf-8 -*-
from uuid import uuid4
from .common import Parser
from ..models.classroom import *

__all__ = [
    "ClassroomParser"
]


class ClassroomParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Classroom:
        year  = int(data["AY"])
        grade = int(data["GRADE"])
        name  = cn if (cn := data["CLASS_NM"]) else uuid4().urn[9:]
        major = data["DDDEP_NM"]
        match data["SCHUL_CRSE_SC_NM"]:
            case "초등학교": course = CourseType.ELEMENTARY
            case "중학교":   course = CourseType.MIDDLE
            case "고등학교": course = CourseType.HIGH
            case "유치원":   course = CourseType.PRESCHOOL
            case _:          course = CourseType.SPECIALITY
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
        match data["DGHT_CRSE_SC_NM"]:
            case "주간": timing = Timing.DAY
            case "야간": timing = Timing.NIGHT
            case _:      timing = None
        return Classroom(
            year=year,
            grade=grade,
            name=name,
            major=major,
            course=course,
            department=department,
            timing=timing,
        )
