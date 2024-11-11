# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Any, Awaitable


class AsyncProperty:
    def __init__(self, fget=None):
        self._fget = fget

    def __get__(self, instance, cls) -> Awaitable[None] | AsyncProperty:
        if instance is None:
            return self
        return self._fget(instance)

    @property
    def fget(self) -> Any | None:
        return self._fget
