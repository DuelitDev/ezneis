from ezneis.types.school import *
from pydantic import BaseModel
from typing import Tuple, Union

__all__ = [
    "SchoolData",
    "NEISOpenAPIData"
]


class SchoolData(BaseModel):
    """

    """
    info:      SchoolInfo
    meal:      Tuple[Meal, ...]
    schedule:  Tuple[SchoolSchedule, ...]
    classroom: Classroom


NEISOpenAPIData = Union[SchoolData, str]
