# -*- coding: utf-8 -*-
from .common import Parser
from ..models.department import *

__all__ = [
    "DepartmentParser"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class DepartmentParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Department:
        # 주야 과정명
        match data["DGHT_CRSE_SC_NM"]:
            case "주간":       timing = Timing.DAY
            case "야간":       timing = Timing.NIGHT
            case "산업체특별": timing = Timing.INDUSTRY_SPECIAL
            case _ as v: raise ValueError(f"처리할 수 없는 주야 과정명: {v}")
        # 계열명
        name = data["ORD_SC_NM"]
        return Department(
            timing=timing,
            name=name,
        )
