# -*- coding: utf-8 -*-
from .common import Parser
from ..models.major import *

__all__ = [
    "MajorParser"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class MajorParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Major:
        # 주야 과정명
        match data["DGHT_CRSE_SC_NM"]:
            case "주간":       timing = Timing.DAY
            case "야간":       timing = Timing.NIGHT
            case "산업체특별": timing = Timing.INDUSTRY_SPECIAL
            case _ as v: raise ValueError(f"처리할 수 없는 주야 과정명: {v}")
        # 계열명
        department = data["ORD_SC_NM"]
        # 학과명
        name = data["DDDEP_NM"]
        return Major(
            timing=timing,
            department=department,
            name=name
        )
