# -*- coding: utf-8 -*-
from __future__ import annotations

import requests
from typing import Optional
from .common import BASE_URL, Services, urljoin
from ..exceptions import (APIKeyMissingException, InternalServiceError,
                          ServiceUnavailableError)

__all__ = [
    "SyncRequest",
]


class SyncRequest:
    def __init__(self, key: Optional[str] = None):
        if not key:
            raise APIKeyMissingException
        self._key = key
        self._maximum_req = 5 if not key else 1000
        self._session = requests.Session()

    def __del__(self):
        self.close()

    def __enter__(self) -> SyncRequest:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get(self, service: Services, *, hint: Optional[int] = None,
            **kwargs) -> list[dict]:
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
                raise InternalServiceError(result["CODE"], result["MESSAGE"])
            head, data = json[service.value]
            if remaining is None:
                remaining = head["head"][0]["list_total_count"]
            buffer.extend(data["row"])
            params["pIndex"] += 1
        return buffer

    def close(self):
        if self._session:
            self._session.close()
