# -*- coding: utf-8 -*-
from __future__ import annotations

import aiohttp
import asyncio
from typing import Optional
from .common import BASE_URL, Services, urljoin
from ..exceptions import (APIKeyMissingException, InternalServiceError,
                          ServiceUnavailableError)

__all__ = [
    "AsyncRequest",
]


class AsyncRequest:
    def __init__(self, key: Optional[str] = None):
        if not key:
            raise APIKeyMissingException
        self._key = key
        self._maximum_req = 5 if not key else 1000
        self._session = aiohttp.ClientSession()

    def __del__(self):
        if not self._session.closed:
            loop = asyncio.get_running_loop()
            asyncio.run_coroutine_threadsafe(self.close(), loop)

    async def __aenter__(self) -> AsyncRequest:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def get(self, service: Services, *, hint: Optional[int] = None,
                  **kwargs) -> list[dict]:
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
                    error = json["RESULT"]
                    raise InternalServiceError(error["CODE"], error["MESSAGE"])
                head, data = json[service.value]
                if remaining is None:
                    remaining = head["head"][0]["list_total_count"]
                row = data["row"]
                remaining -= len(row)
                return row

        if hint is None:
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
