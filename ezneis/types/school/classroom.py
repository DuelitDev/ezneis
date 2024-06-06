from enum import Enum, auto
from pydantic import BaseModel
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Optional, Tuple

__all__ = [
    "ClassCourse",
    "ClassDetailCourse",
    "ClassTimeClassification",
    "ClassInfo",
    "Classroom",
]


class ClassCourse(Enum):
    """
    Enumeration for different types of school courses.
    """
    PRESCHOOL  = auto()
    """Preschool level education."""
    ELEMENTARY = auto()
    """Elementary school level education."""
    MIDDLE     = auto()
    """Middle school level education."""
    HIGH       = auto()
    """High school level education."""
    SPECIALITY = auto()
    """Specialized courses not falling under the traditional levels."""


class ClassDetailCourse(Enum):
    """
    Enumeration for specific types of detailed courses within a school.
    """
    NORMAL        = auto()
    """Standard education."""
    VOCATIONAL    = auto()
    """Vocational education."""
    SPECIALIZED   = auto()
    """Specialized education."""
    INTERNATIONAL = auto()
    """International education curriculum."""
    BUSINESS      = auto()
    """Business education."""
    COMMERCE      = auto()
    """Commerce education."""
    TECHNICAL     = auto()
    """Technical education."""
    AGRICULTURE   = auto()
    """Agriculture-focused education."""
    FISHERIES     = auto()
    """Fisheries-related courses."""
    INTEGRATED    = auto()
    """Integrated education programs."""
    LANGUAGE      = auto()
    """Language-focused education."""
    SCIENCE       = auto()
    """Science-focused education."""
    PHYSICAL      = auto()
    """Physical education."""
    ART           = auto()
    """Art-focused education."""
    ALTERNATIVE   = auto()
    """Alternative education programs."""
    TRAINING      = auto()
    """Training-specific courses."""
    NONE          = auto()
    """No specific detailed course."""


class ClassTimeClassification(Enum):
    """
    Enumeration representing the classification of a class based on time.
    """
    DAY = auto()
    """Represents a daytime classes."""
    NIGHT = auto()
    """Represents a nighttime classes."""
    NONE = auto()
    """Represents no specific time classification."""


class ClassInfo(BaseModel):
    """
    Model for representing information about a class.
    """
    year:          int
    """The year the class is being conducted."""
    grade:         int
    """The grade level of the class."""
    name:          Optional[str]
    """The name of the class."""
    department:    Optional[str]
    """The department offering the class."""
    course:        ClassCourse
    """The type of course."""
    course_detail: ClassDetailCourse
    """The detailed type of course."""
    time:          ClassTimeClassification
    """The time classification of the class."""


class Classroom(dict):
    """
    A dictionary-like class representing a collection of classes.
    """
    @classmethod
    def __validator__(cls, obj: Any, _: core_schema.ValidationInfo) -> Any:
        """
        Validates that the object is a Classroom instance and that
        its keys are tuples of (int, str) and values are ClassInfo instances.

        :param obj: The object to validate.
        :return: The validated object if valid.
        :except ValueError: If the object or its elements are not valid.
        """
        if isinstance(obj, Classroom):
            for k in obj.keys():
                if not isinstance(k[0], int) or not isinstance(k[1], str):
                    raise ValueError("Invalid key format. "
                                     "Expected a tuple of (int, str).")
            for v in obj.values():
                if not isinstance(v, ClassInfo):
                    raise ValueError("Invalid value type. "
                                     "Expected a ClassInfo instance.")
            return obj
        raise ValueError("Invalid object type. "
                         "Expected a Classroom instance.")

    @classmethod
    def __get_pydantic_core_schema__(cls, *_, **__) -> CoreSchema:
        """
        Returns the Pydantic core schema for the Classroom class.

        :return: The Pydantic core schema.
        """
        return core_schema.with_info_plain_validator_function(cls.__validator__)

    def __init__(self, classes: Tuple[ClassInfo, ...]):
        """
        Initializes the Classroom with a tuple of ClassInfo objects.

        :param classes: A tuple of ClassInfo objects.
        """
        for c in classes:
            self[(c.grade, c.name)] = c
        super().__init__()

    def __getitem__(self, key):
        """
        Retrieves class information by grade.
        If an integer between 0 and 7 is provided,
        it returns a dictionary of classes for that grade.

        :param key: The grade to retrieve classes for.
        :return: A dictionary of class names to ClassInfo objects
                 for the specified grade.
        """
        if isinstance(key, int) and 0 <= key <= 7:
            return {c.name: c for c in self.values() if c.grade == key}

    @property
    def grade0(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 0.

        :return: A dictionary of class names to ClassInfo objects for grade 0.
        """
        return {c.name: c for c in self.values() if c.grade == 0}

    @property
    def grade1(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 1.

        :return: A dictionary of class names to ClassInfo objects for grade 1.
        """
        return {c.name: c for c in self.values() if c.grade == 1}

    @property
    def grade2(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 2.

        :return: A dictionary of class names to ClassInfo objects for grade 2.
        """
        return {c.name: c for c in self.values() if c.grade == 2}

    @property
    def grade3(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 3.

        :return: A dictionary of class names to ClassInfo objects for grade 3.
        """
        return {c.name: c for c in self.values() if c.grade == 3}

    @property
    def grade4(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 4.

        :return: A dictionary of class names to ClassInfo objects for grade 4.
        """
        return {c.name: c for c in self.values() if c.grade == 4}

    @property
    def grade5(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 5.

        :return: A dictionary of class names to ClassInfo objects for grade 5.
        """
        return {c.name: c for c in self.values() if c.grade == 5}

    @property
    def grade6(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 6.

        :return: A dictionary of class names to ClassInfo objects for grade 6.
        """
        return {c.name: c for c in self.values() if c.grade == 6}

    @property
    def grade7(self) -> Dict[str, ClassInfo]:
        """
        Returns a dictionary of classes for grade 7.

        :return: A dictionary of class names to ClassInfo objects for grade 7.
        """
        return {c.name: c for c in self.values() if c.grade == 7}
