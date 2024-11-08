# -*- coding: utf-8 -*-
from typing import Any, Awaitable, Self


class AsyncProperty:
    def __init__(self, fget=None):
        self._fget = fget

    def __get__(self, instance, cls) -> Awaitable[None] | Self:
        if instance is None:
            return self
        return self._fget(instance)

    @property
    def fget(self) -> Any | None:
        return self._fget
