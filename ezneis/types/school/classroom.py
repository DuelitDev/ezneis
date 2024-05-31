from enum import Enum, auto
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Optional, Tuple

__all__ = [
    "ClassCourse",
    "ClassDetailCourse",
    "ClassPartTime",
    "ClassInfo",
    "Classroom",
]


class ClassCourse(Enum):
    """

    """
    PRESCHOOL  = auto()
    ELEMENTARY = auto()
    MIDDLE     = auto()
    HIGH       = auto()
    SPECIALITY = auto()


class ClassDetailCourse(Enum):
    """

    """
    NORMAL        = auto()
    VOCATIONAL    = auto()
    SPECIALIZED   = auto()
    INTERNATIONAL = auto()
    BUSINESS      = auto()
    COMMERCE      = auto()
    TECHNICAL     = auto()
    AGRICULTURE   = auto()
    FISHERIES     = auto()
    INTEGRATED    = auto()
    LANGUAGE      = auto()
    SCIENCE       = auto()
    PHYSICAL      = auto()
    ART           = auto()
    ALTERNATIVE   = auto()
    TRAINING      = auto()
    NONE          = auto()


class ClassPartTime(Enum):
    """

    """
    DAY   = auto()
    NIGHT = auto()
    NONE  = auto()


class ClassInfo(BaseModel):
    """

    """
    year:          int
    grade:         int
    name:          Optional[str]
    department:    Optional[str]
    course:        ClassCourse
    course_detail: ClassDetailCourse
    part_time:     ClassPartTime


class Classroom(dict):
    """

    """
    @classmethod
    def __validator__(cls, obj: Any, _: core_schema.ValidationInfo) -> Any:
        if isinstance(obj, Classroom):
            for k in obj.keys():
                if not isinstance(k[0], int) or not isinstance(k[1], str):
                    raise ValueError
            for v in obj.values():
                if not isinstance(v, ClassInfo):
                    raise ValueError
            return obj
        raise ValueError

    @classmethod
    def __get_pydantic_core_schema__(cls, *_, **__) -> CoreSchema:
        return core_schema.with_info_plain_validator_function(cls.__validator__)

    def __init__(self, classes: Tuple[ClassInfo, ...]):
        for c in classes:
            self[(c.grade, c.name)] = c
        super().__init__()

    def __getitem__(self, key):
        if isinstance(key, int) and 0 <= key <= 7:
            return {c.name: c for c in self.values() if c.grade == key}


    @property
    def grade0(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 0}

    @property
    def grade1(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 1}

    @property
    def grade2(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 2}

    @property
    def grade3(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 3}

    @property
    def grade4(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 4}

    @property
    def grade5(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 5}

    @property
    def grade6(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 6}

    @property
    def grade7(self) -> Dict[str, ClassInfo]:
        """

        :return:
        """
        return {c.name: c for c in self.values() if c.grade == 7}
