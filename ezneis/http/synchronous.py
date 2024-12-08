# -*- coding: utf-8 -*-
from __future__ import annotations

import requests
from typing import Optional
from .common import BASE_URL, MAX_CACHE, TIME_TO_LIVE, Services, urljoin
from ..exceptions import (InternalServiceCode, InternalServiceError,
                          ServiceUnavailableError, SessionClosedException)
from ..utils.caches import ttl_cache

__all__ = [
    "SyncSession",
]


class SyncSession:
    def __init__(self, key: str):
        self._key = key
        self._maximum_req = 5 if not key else 1000
        self._session = requests.Session()
        self._closed = False

    def __del__(self):
        self.close()

    def __enter__(self) -> SyncSession:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def closed(self) -> bool:
        return self._closed

    @ttl_cache(ttl=TIME_TO_LIVE, maxsize=MAX_CACHE, is_method=True)
    def get(self, service: Services, *, hint: Optional[int] = None,
            **kwargs) -> list[dict]:
        if self.closed:
            raise SessionClosedException
        url = urljoin(BASE_URL, service.value)
        params = {
            **kwargs,
            "KEY": self._key,
            "Type": "json",
            "pIndex": 1,
            "pSize": (hint if hint and hint <= self._maximum_req
                      else self._maximum_req),
        }
        buffer = []
        remaining = hint
        while remaining is None or remaining - len(buffer) > 0:
            response = self._session.get(url, params=params)
            if response.status_code != 200:
                raise ServiceUnavailableError(url)
            json = response.json()
            if service.value not in json:
                result = json["RESULT"]
                code, message = result["CODE"], result["MESSAGE"]
                if code == InternalServiceCode.NOT_FOUND.value:
                    break
                raise InternalServiceError(code, message)
            head, data = json[service.value]
            if remaining is None:
                remaining = head["head"][0]["list_total_count"]
            buffer.extend(data["row"])
            params["pIndex"] += 1
        return buffer

    def close(self):
        if self._session:
            self._session.close()
            self._closed = True
