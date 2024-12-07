# -*- coding: utf-8 -*-
from datetime import datetime
from re import compile as regexp_compile
from .common import Parser
from ..models.meal import *

__all__ = [
    "MealParser"
]

KCAL_PATTERN = regexp_compile(r"[0-9]*[.][0-9]")
UNIT_PATTERN = regexp_compile(r"\((.*?)\)")


class MealParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Meal:
        dishes = []
        raw = r.split("<br/>") if (r := data["DDISH_NM"]) is not None else []
        for dish in raw:
            name, *_, info = dish.split(' ')
            name = name.replace('*', '').replace('@', '')
            allergies = tuple(Allergy(int(x)) for x in
                              info[1:-1].split('.') if x)
            dishes.append(Dish(name=name, allergies=allergies))
        dishes = tuple(dishes)
        nutrients = []
        raw = r.split("<br/>") if (r := data["NTR_INFO"]) is not None else []
        for ntr in raw:
            tmp, value = ntr.split(" : ")
            name = tmp[:tmp.find('(')].strip()
            unit = UNIT_PATTERN.findall(ntr)[0]
            nutrients.append(Nutrient(name=name, unit=unit, value=float(value)))
        nutrients = tuple(nutrients)
        origins = []
        raw = r.split("<br/>") if (r := data["ORPLC_INFO"]) is not None else []
        for org in raw:
            name, country = org.rsplit(" : ", 1)
            origins.append(Origin(name=name, origin=country))
        origins = tuple(origins)
        headcount = int(float(data["MLSV_FGR"]))
        kcal = float(KCAL_PATTERN.findall(data["CAL_INFO"])[0])
        date = datetime.strptime(data["MLSV_YMD"], "%Y%m%d").date()
        time = MealTime(int(data["MMEAL_SC_CODE"]))
        return Meal(
            dishes=dishes,
            nutrients=nutrients,
            origins=origins,
            headcount=headcount,
            kcal=kcal,
            date=date,
            time=time
        )
