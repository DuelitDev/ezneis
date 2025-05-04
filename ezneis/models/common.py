# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Sequence
from ..http import AsyncSession, SyncSession

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

    @abstractmethod
    def fetch_sync(self, sess: SyncSession) -> Sequence[CoreModel]:
        pass

    @abstractmethod
    async def fetch_async(self, sess: AsyncSession) -> Sequence[CoreModel]:
        pass
