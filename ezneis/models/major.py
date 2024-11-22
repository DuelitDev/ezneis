# -*- coding: utf-8 -*-
from dataclasses import dataclass

__all__ = [
    "Major"
]


@dataclass(frozen=True)
class Major:
    name: str