# -*- coding: utf-8 -*-
from .common import Parser
from ..models.major import *

__all__ = [
    "MajorParser"
]


class MajorParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> Major:
        return Major(name=data["DDDEP_NM"])
