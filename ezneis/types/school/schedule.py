from datetime import date
from enum import Enum, auto
from pydantic import BaseModel
from typing import Optional, SupportsIndex, Union

__all__ = [
    "SchedulePartTime",
    "EventType",
    "EventCorresponds",
    "SchoolSchedule"
]


class SchedulePartTime(Enum):
    """

    """
    DAY   = auto()
    NIGHT = auto()
    NONE  = auto()


class EventType(Enum):
    """

    """
    DAY_OFF = auto()
    HOLIDAY = auto()
    NONE    = auto()


class EventCorresponds(BaseModel):
    """

    """
    grade1: bool
    grade2: bool
    grade3: bool
    grade4: bool
    grade5: bool
    grade6: bool

    def __getitem__(self, indices: Union[slice, SupportsIndex]):
        return (self.grade1, self.grade2, self.grade3,
                self.grade4, self.grade5, self.grade6)[indices]


class SchoolSchedule(BaseModel):
    """

    """
    year:        int
    part_time:   SchedulePartTime
    name:        str
    description: Optional[str]
    corresponds: EventCorresponds
    type:        EventType
    date:        date

