# -*- coding: utf-8 -*-
from ..models.department import *
from .common import Parser

__all__ = ["DepartmentParser"]


class DepartmentParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Department:
        # 주야 과정명
        match data["DGHT_CRSE_SC_NM"]:
            case "주간":
                timing = Timing.DAY
            case "야간":
                timing = Timing.NIGHT
            case "산업체특별":
                timing = Timing.INDUSTRY_SPECIAL
            case _ as v:
                raise ValueError(f"처리할 수 없는 주야 과정명: {v}")
        # 계열명
        name = data["ORD_SC_NM"]
        return Department(
            timing=timing,
            name=name,
        )
