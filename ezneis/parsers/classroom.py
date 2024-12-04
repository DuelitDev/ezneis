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
        department = data["ORD_SC_NM"]
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
