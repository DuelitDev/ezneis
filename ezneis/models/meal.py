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
    "Meal"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class Allergy(Enum):
    """
    식품 알레르기 열거형입니다.
    """
    EGG = 1
    """난류에 의한 식품 알레르기입니다."""
    MILK = 2
    """우유에 의한 식품 알레르기입니다."""
    BUCKWHEAT = 3
    """매밀에 의한 식품 알레르기입니다."""
    PEANUT = 4
    """땅콩에 의한 식품 알레르기입니다."""
    SOYBEAN = 5
    """대두에 의한 식품 알레르기입니다."""
    WHEAT = 6
    """밀에 의한 식품 알레르기입니다."""
    MACKEREL = 7
    """고등어에 의한 식품 알레르기입니다."""
    CRAB = 8
    """게에 의한 식품 알레르기입니다."""
    SHRIMP = 9
    """새우에 의한 식품 알레르기입니다."""
    PORK = 10
    """돼지고기에 의한 식품 알레르기입니다."""
    PEACH = 11
    """복숭아에 의한 식품 알레르기입니다."""
    TOMATO = 12
    """토마토에 의한 식품 알레르기입니다."""
    SULFITE = 13
    """아황산류에 의한 식품 알레르기입니다."""
    WALNUT = 14
    """호두에 의한 식품 알레르기입니다."""
    CHICKEN = 15
    """닭고기에 의한 식품 알레르기입니다."""
    BEEF = 16
    """쇠고기에 의한 식품 알레르기입니다."""
    CALAMARI = 17
    """오징어에 의한 식품 알레르기입니다."""
    SHELLFISH = 18
    """조개류(굴, 전복, 홍합 포함)에 의한 식품 알레르기입니다."""
    PINE_NUT = 19
    """잣에 의한 식품 알레르기입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
class MealTime(Enum):
    """
    급식 시간 열거형입니다.
    """
    BREAKFAST = 1
    """조식입니다."""
    LUNCH = 2
    """중식입니다."""
    DINNER = 3
    """석식입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Dish:
    """
    요리 정보를 나타내는 데이터 클래스입니다.
    """
    name: str
    """요리 이름입니다."""
    allergies: tuple[Allergy, ...]
    """요리에 의한 발생 가능성이 있는 식품 알레르기입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Nutrient:
    """
    영양 정보를 나타내는 데이터 클래스입니다.
    """
    name: str
    """영양 이름입니다."""
    unit: str
    """단위입니다."""
    value: float
    """양입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Origin:
    """
    원산지 정보를 나타내는 데이터 클래스입니다.
    """
    name: str
    """재료 이름입니다."""
    origin: str
    """원산지 이름입니다."""


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
@dataclass(frozen=True)
class Meal:
    """
    급식 식단 정보를 나타내는 데이터 클래스입니다.
    """
    time: MealTime
    """급식 시간 (식사 코드)"""
    date: date
    """급식 일자"""
    headcount: int
    """급식 인원 수"""
    dishes: tuple[Dish, ...]
    """요리명"""
    origins: tuple[Origin, ...]
    """원산지 정보"""
    kcal: float
    """칼로리 정보"""
    nutrients: tuple[Nutrient, ...]
    """영양 정보"""
