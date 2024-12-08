# -*- coding: utf-8 -*-
from __future__ import annotations

import aiohttp
import asyncio
from typing import Optional
from .common import BASE_URL, MAX_CACHE, TIME_TO_LIVE, Services, urljoin
from ..exceptions import (InternalServiceCode, InternalServiceError,
                          ServiceUnavailableError, SessionClosedException)
from ..utils.caches import ttl_cache

__all__ = [
    "AsyncSession",
]


class AsyncSession:
    def __init__(self, key: str):
        self._key = key
        self._maximum_req = 5 if not key else 1000
        self._session = aiohttp.ClientSession()
        self._closed = False

    def __del__(self):
        if not self._session.closed:
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            asyncio.run_coroutine_threadsafe(self.close(), loop)

    async def __aenter__(self) -> AsyncSession:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    @property
    def closed(self) -> bool:
        return self._session.closed and self._closed

    @ttl_cache(ttl=TIME_TO_LIVE, maxsize=MAX_CACHE, is_method=True)
    async def get(self, service: Services, *, hint: Optional[int] = None,
                  **kwargs) -> list[dict]:
        if self.closed:
            raise SessionClosedException
        url = urljoin(BASE_URL, service.value)
        params = {
            **kwargs,
            "KEY": self._key,
            "Type": "json",
            "pSize": (hint if hint and hint <= self._maximum_req
                      else self._maximum_req),
        }
        buffer = []
        remaining = hint

        async def task(index: int = 1) -> list[dict]:
            nonlocal url, params, remaining
            params["pIndex"] = index
            async with self._session.get(url, params=params) as response:
                if response.status != 200:
                    raise ServiceUnavailableError(url)
                json = await response.json()
                if service.value not in json:
                    result = json["RESULT"]
                    code, message = result["CODE"], result["MESSAGE"]
                    if code == InternalServiceCode.NOT_FOUND.value:
                        if remaining is None:
                            remaining = 0
                        return []
                    raise InternalServiceError(code, message)
                head, data = json[service.value]
                if remaining is None:
                    remaining = head["head"][0]["list_total_count"]
                row = data["row"]
                remaining -= len(row)
                return row

        if hint is not None:
            pages = (remaining // self._maximum_req
                     + int(remaining % self._maximum_req != 0))
            tasks = [task(p) for p in range(1, pages + 1)]
        else:
            buffer.extend(await task())
            if remaining <= 0:
                return buffer
            pages = (remaining // self._maximum_req
                     + int(remaining % self._maximum_req != 0))
            tasks = [task(p) for p in range(2, pages + 2)]
        for t in await asyncio.gather(*tasks):
            buffer.extend(t)
        return buffer

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()
            self._closed = True
