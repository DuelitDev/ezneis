# -*- coding: utf-8 -*-
from uuid import uuid4
from .common import Parser
from ..models.lecture_room import *

__all__ = [
    "LectureRoomParser"
]


class LectureRoomParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> LectureRoom:
        year = int(data["AY"])
        grade = int(data["GRADE"])
        semester = int(data["SEM"])
        name = cn if (cn := data["CLRM_NM"]) else uuid4().urn[9:]
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
        return LectureRoom(
            year=year,
            grade=grade,
            semester=semester,
            name=name,
            major=major,
            course=course,
            department=department,
            timing=timing
        )
