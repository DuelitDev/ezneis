# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Sequence
from ..http import SyncSession, AsyncSession, Service

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
        self._limit: int | None = None

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
    def _service(self) -> Service:
        pass

    @property
    @abstractmethod
    def _model(self) -> type[CoreModel]:
        pass

    def limit(self, limit: int) -> CoreBuilder:
        self._limit = limit
        return self

    def fetch(self, sess: SyncSession) -> Sequence[CoreModel]:
        return tuple(
            self._model.from_dict(i)
            for i in sess.get(self._service, limit=self._limit, **self._param)
        )

    async def fetch_async(self, sess: AsyncSession) -> Sequence[CoreModel]:
        return tuple(
            self._model.from_dict(i)
            for i in await sess.get(self._service, limit=self._limit, **self._param)
        )
