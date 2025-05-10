# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from ..http import Service

__all__ = ["CoreModel", "CoreBuilder"]


@dataclass(frozen=True)
class CoreModel(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> CoreModel:
        pass


class CoreBuilder(metaclass=ABCMeta):
    def __init__(self):
        self._param = {}

    def __copy__(self):
        new = self.__class__()
        new._param = self._param.copy()
        return new

    def copy(self) -> CoreBuilder:
        return self.__copy__()

    def reset(self) -> CoreBuilder:
        self._param.clear()
        return self

    @property
    @abstractmethod
    def service(self) -> Service:
        pass
