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
        for dish in data["DDISH_NM"].split("<br/>"):
            name, *_, info = dish.split(' ')
            name = name.replace('*', '').replace('@', '')
            allergies = tuple(Allergy(int(x)) for x in
                              info[1:-1].split('.') if x)
            dishes.append(Dish(name=name, allergies=allergies))
        dishes = tuple(dishes)
        nutrients = []
        for ntr in data["NTR_INFO"].split("<br/>"):
            tmp, value = ntr.split(" : ")
            name = tmp[:tmp.find('(')].strip()
            unit = UNIT_PATTERN.findall(ntr)[0]
            nutrients.append(Nutrient(name=name, unit=unit, value=float(value)))
        nutrients = tuple(nutrients)
        origins = []
        for org in data["ORPLC_INFO"].split("<br/>"):
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
