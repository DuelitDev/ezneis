# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from enum import Enum

__all__ = [
    "Allergy",
    "MealTime",
    "Dish",
    "Nutrient",
    "Origin",
    "Meal",
]


class Allergy(Enum):
    """
    An enumeration of common food allergies.
    Each member represents a type of food that can cause allergic reactions.
    """
    EGG = 1
    """Allergy to eggs."""
    MILK = 2
    """Allergy to milk."""
    BUCKWHEAT = 3
    """Allergy to buckwheat."""
    PEANUT = 4
    """Allergy to peanuts."""
    SOYBEAN = 5
    """Allergy to soybeans."""
    WHEAT = 6
    """Allergy to wheat."""
    MACKEREL = 7
    """Allergy to mackerel."""
    CRAB = 8
    """Allergy to crab."""
    SHRIMP = 9
    """Allergy to shrimp."""
    PORK = 10
    """Allergy to pork."""
    PEACH = 11
    """Allergy to peaches."""
    TOMATO = 12
    """Allergy to tomatoes."""
    SULFITE = 13
    """Allergy to sulfites."""
    WALNUT = 14
    """Allergy to walnuts."""
    CHICKEN = 15
    """Allergy to chicken."""
    BEEF = 16
    """Allergy to beef."""
    CALAMARI = 17
    """Allergy to calamari."""
    SHELLFISH = 18
    """Allergy to shellfish."""
    PINE_NUT = 19
    """Allergy to pine nuts."""


class MealTime(Enum):
    """
    An enumeration of meal times.
    Each member represents a typical time of day for a meal.
    """
    BREAKFAST = 1
    """Time for breakfast."""
    LUNCH = 2
    """Time for lunch."""
    DINNER = 3
    """Time for dinner."""


@dataclass(frozen=True)
class Dish:
    """
    A model representing a dish in a meal.
    """
    name: str
    """The name of the dish."""
    allergies: tuple[Allergy, ...]
    """The allergies associated with the dish."""


@dataclass(frozen=True)
class Nutrient:
    """
    A model representing a nutrient in a meal.
    """
    name: str
    """The name of the nutrient."""
    unit: str
    """The unit of measurement for the nutrient."""
    value: float
    """The amount of the nutrient."""


@dataclass(frozen=True)
class Origin:
    """
    A model representing the origin of an ingredient in a meal.
    """
    name: str
    """The name of the ingredient."""
    origin: str
    """The geographic origin of the ingredient."""


@dataclass(frozen=True)
class Meal:
    """
    A model representing a meal.
    """
    dishes: tuple[Dish, ...]
    """The dishes included in the meal."""
    nutrients: tuple[Nutrient, ...]
    """The nutrients included in the meal."""
    origins: tuple[Origin, ...]
    """The origin of the meal's ingredients."""
    headcount: int
    """The number of people who received the meal."""
    kcal: float
    """The total calorie content of the meal."""
    date: date
    """The date the meal is served."""
    time: MealTime
    """The time of day the meal is served."""
