from datetime import datetime
from ezneis.parser.core import *
from ezneis.types.school.meal import *
from typing import Tuple
import re

__all__ = [
    "SchoolMealParser"
]

_R_P1_KCAL     = re.compile(r"[0-9]*[.][0-9]")
_R_P1_NTR_UNIT = re.compile(r"\((.*?)\)")


class SchoolMealParser(Parser):
    @classmethod
    def parse(cls, data) -> Tuple[Meal, ...]:
        """

        :param data:
        :return:
        """
        return tuple(cls._run_parsers(row) for row in
                     data.mealServiceDietInfo[1].row)

    @staticmethod
    def _parser1(r) -> Meal:
        """

        :param r:
        :return:
        """
        dishes = []
        for dish in r.DDISH_NM.split("<br/>"):
            name, *_, info = dish.split(' ')
            name = (name.replace('*', '')
                        .replace('@', ''))
            allergies = tuple(Allergy(int(x)) for x in
                              info[1:-1].split('.') if x)
            dishes.append(Dish(name=name, allergies=allergies))
        nutrients = []
        for ntr in r.NTR_INFO.split("<br/>"):
            tmp, value = ntr.split(" : ")
            name = tmp[:tmp.find('(')].strip()
            unit = _R_P1_NTR_UNIT.findall(ntr)[0]
            nutrients.append(Nutrient(name=name, unit=unit, value=float(value)))
        origin = []
        for org in r.ORPLC_INFO.split("<br/>"):
            name, country = org.rsplit(" : ", 1)
            origin.append(Origin(name=name, origin=country))
        headcount = float(r.MLSV_FGR)
        kcal      = float(_R_P1_KCAL.findall(r.CAL_INFO)[0])
        date      = datetime.strptime(r.MLSV_YMD, "%Y%m%d").date()
        time      = MealTime(int(r.MMEAL_SC_CODE))

        return Meal(
            dishes=dishes,
            nutrients=nutrients,
            origin=origin,
            headcount=headcount,
            kcal=kcal,
            date=date,
            time=time
        )

    _parsers = (_parser1,)
