from asyncio import gather
from ezneis.api.core import *
from ezneis.types import *
from ezneis.util import *
from functools import lru_cache
from typing import Tuple

__all__ = [
    "SyncAPI",
    "CoAPI"
]


class SyncAPI:
    @classmethod
    @lru_cache(maxsize=1)
    def fetch(cls, name: str, key: str = "",
              region: Region = Region.UNSPECIFIED, *,
              no_check: bool = False, **kwargs
              ) -> NEISOpenAPIData:
        """

        :param name: School name or code.
        :param key: API key.
        :param region: School region.
        :param no_check: Do not validate school name.
        :return: A school data.
        """
        if not no_check:
            identifiers = SyncAPIFetch.get_school_id(key, name, region)
        else:
            identifiers = ((name, region),)
        c, r = identifiers[0]
        _info = SyncAPIFetch.fetch_school_info(key, c, r)
        _meal = SyncAPIFetch.fetch_meal(
            key, c, r, **kwargs.get("meal", {}))
        _schedule = SyncAPIFetch.fetch_schedule(
            key, c, r, **kwargs.get("schedule", {}))
        _classroom = SyncAPIFetch.fetch_class(
            key, c, r, **kwargs.get("classroom", {})
        )
        return SchoolData(
            info=_info,
            meal=_meal,
            schedule=_schedule,
            classroom=_classroom
        )

    @classmethod
    @lru_cache(maxsize=1)
    def fetch_all(cls, name: str, key: str = "",
                  region: Region = Region.UNSPECIFIED, **kwargs
                  ) -> Tuple[NEISOpenAPIData, ...]:
        """

        :param name: School name or code.
        :param key: API key.
        :param region: School region.
        :return: A school data.
        """
        identifiers = SyncAPIFetch.get_school_id(key, name, region)
        temp = []
        for c, r in identifiers:
            data = cls.fetch(c, key, r, no_check=True, **kwargs)
            temp.append(data)
        return tuple(temp)


class CoAPI:
    @classmethod
    @lru_cache(maxsize=1)
    async def fetch(cls, name: str, key: str = "",
                    region: Region = Region.UNSPECIFIED, *,
                    no_check: bool = False, **kwargs
                    ) -> NEISOpenAPIData:
        """

        :param name: School name or code.
        :param key: API key.
        :param region: School region.
        :param no_check: Do not validate school name.
        :return: A school data.
        """
        if not no_check:
            identifiers = await CoAPIFetch.get_school_id(key, name, region)
        else:
            identifiers = ((name, region),)
        c, r = identifiers[0]
        _info_task = CoAPIFetch.fetch_school_info(key, c, r)
        _meal_task = CoAPIFetch.fetch_meal(
            key, c, r, **kwargs.get("meal", {}))
        _schedule_task = CoAPIFetch.fetch_schedule(
            key, c, r, **kwargs.get("schedule", {}))
        _classroom_task = CoAPIFetch.fetch_class(
            key, c, r, **kwargs.get("classroom", {}))
        _info, _meal, _schedule, _classroom = await gather(
            _info_task, _meal_task, _schedule_task, _classroom_task
        )
        return SchoolData(
            info=_info,
            meal=_meal,
            schedule=_schedule,
            classroom=_classroom
        )

    @classmethod
    @lru_cache(maxsize=1)
    async def fetch_all(cls, name: str, key: str = "",
                        region: Region = Region.UNSPECIFIED, **kwargs
                        ) -> Tuple[NEISOpenAPIData, ...]:
        """

        :param name: School name or code.
        :param key: API key.
        :param region: School region.
        :return: A school data.
        """
        identifiers = await CoAPIFetch.get_school_id(key, name, region)
        tasks = []
        for c, r in identifiers:
            task = cls.fetch(c, key, r, no_check=True, **kwargs)
            tasks.append(task)
        return await gather(*tasks)
