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
    Enumeration of common food allergies.
    Each member represents a type of food that can cause allergic reactions.
    """
    EGG       = 1
    """Allergy to eggs."""
    MILK      = 2
    """Allergy to milk."""
    BUCKWHEAT = 3
    """Allergy to buckwheat."""
    PEANUT    = 4
    """Allergy to peanuts."""
    SOYBEAN   = 5
    """Allergy to soybeans."""
    WHEAT     = 6
    """Allergy to wheat."""
    MACKEREL  = 7
    """Allergy to mackerel."""
    CRAB      = 8
    """Allergy to crab."""
    SHRIMP    = 9
    """Allergy to shrimp."""
    PORK      = 10
    """Allergy to pork."""
    PEACH     = 11
    """Allergy to peaches."""
    TOMATO    = 12
    """Allergy to tomatoes."""
    SULFITE   = 13
    """Allergy to sulfites."""
    WALNUT    = 14
    """Allergy to walnuts."""
    CHICKEN   = 15
    """Allergy to chicken."""
    BEEF      = 16
    """Allergy to beef."""
    CALAMARI  = 17
    """Allergy to calamari."""
    SHELLFISH = 18
    """Allergy to shellfish."""
    PINENUT   = 19
    """Allergy to pine nuts."""


class MealTime(Enum):
    """
    Enumeration of meal times.
    Each member represents a typical time of day for a meal.
    """
    BREAKFAST = 1
    """Represents breakfast time."""
    LUNCH     = 2
    """Represents lunch time."""
    DINNER    = 3
    """Represents dinner time."""


class Dish(BaseModel):
    """
    Model representing a dish in a meal.
    """
    name:      str
    """The name of the dish."""
    allergies: Tuple[Allergy, ...]
    """The allergies associated with the dish."""


class Nutrient(BaseModel):
    """
    Model representing a nutrient in a meal.
    """
    name:  str
    """The name of the nutrient."""
    unit:  str
    """The unit of measurement for the nutrient."""
    value: float
    """The amount of the nutrient."""


class Origin(BaseModel):
    """
    Model representing the origin of an ingredient in a meal.
    """
    name:   str
    """The name of the ingredient."""
    origin: str
    """The place of origin of the ingredient."""


class Meal(BaseModel):
    """
    Model representing a meal.
    """
    dishes:    Tuple[Dish, ...]
    """The dishes included in the meal."""
    nutrients: Tuple[Nutrient, ...]
    """The nutrients included in the meal."""
    origin:    Tuple[Origin, ...]
    """The origin of the meal."""
    headcount: int
    """The number of people who received the meal."""
    kcal:      float
    """The total calorie content of the meal."""
    date:      date
    """The date the meal is served."""
    time:      MealTime
    """The time of day the meal is served."""
