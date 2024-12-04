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
        name = data["ORD_SC_NM"] if "ORD_SC_NM" in data else None
        match data["DGHT_CRSE_SC_NM"]:
            case "주간":       timing = Timing.DAY
            case "야간":       timing = Timing.NIGHT
            case "산업체특별": timing = Timing.BOTH
            case _:            timing = None
        is_special_industry_timing = timing == Timing.BOTH
        return Department(
            name=name,
            timing=timing,
            is_special_industry_timing=is_special_industry_timing
        )
