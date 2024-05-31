from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Tuple

__all__ = [
    "Allergy",
    "MealTime",
    "Dish",
    "Nutrient",
    "Origin",
    "Meal"
]


class Allergy(Enum):
    """

    """
    EGG       = 1
    MILK      = 2
    BUCKWHEAT = 3
    PEANUT    = 4
    SOYBEAN   = 5
    WHEAT     = 6
    MACKEREL  = 7
    CRAB      = 8
    SHRIMP    = 9
    PORK      = 10
    PEACH     = 11
    TOMATO    = 12
    SULFITE   = 13
    WALNUT    = 14
    CHICKEN   = 15
    BEEF      = 16
    CALAMARI  = 17
    SHELLFISH = 18
    PINENUT   = 19


class MealTime(Enum):
    """

    """
    BREAKFAST = 1
    LUNCH     = 2
    DINNER    = 3


class Dish(BaseModel):
    """

    """
    name:      str
    allergies: Tuple[Allergy, ...]


class Nutrient(BaseModel):
    """

    """
    name:  str
    unit:  str
    value: float


class Origin(BaseModel):
    """

    """
    name:   str
    origin: str


class Meal(BaseModel):
    """

    """
    dishes:    Tuple[Dish, ...]
    nutrients: Tuple[Nutrient, ...]
    origin:    Tuple[Origin, ...]
    headcount: int
    kcal:      float
    date:      date
    time:      MealTime
