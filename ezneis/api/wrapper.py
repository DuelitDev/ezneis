from asyncio import gather
from ezneis.api.core import *
from ezneis.types import *
from ezneis.util import *
from typing import Tuple

__all__ = [
    "SyncAPI",
    "CoAPI"
]


class SyncAPI:
    """

    """

    @classmethod
    def fetch(cls, name: str, key: str = "",
              region: Region = Region.UNSPECIFIED, *,
              no_check: bool = False, **kwargs
              ) -> NEISOpenAPIData:
        """
        Fetches NEIS API data.

        :param name: School or Academy name.
        :param key: The API key used to authenticate the request.
        :param region: The region of the school or academy.
        :param no_check: Whether to perform code check.
        :param kwargs: Additional parameters for fetching data.
        :return: Fetched data from NEIS API.
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
    def fetch_all(cls, name: str, key: str = "",
                  region: Region = Region.UNSPECIFIED, **kwargs
                  ) -> Tuple[NEISOpenAPIData, ...]:
        """
        Fetches NEIS API data for all schools or academies.

        :param name: School or Academy name.
        :param key: The API key used to authenticate the request.
        :param region: The region of the school or academy.
        :param kwargs: Additional parameters for fetching data.
        :return: Fetched data from NEIS API.
        """
        identifiers = SyncAPIFetch.get_school_id(key, name, region)
        temp = []
        for c, r in identifiers:
            data = cls.fetch(c, key, r, no_check=True, **kwargs)
            temp.append(data)
        return tuple(temp)


class CoAPI:
    @classmethod
    async def fetch(cls, name: str, key: str = "",
                    region: Region = Region.UNSPECIFIED, *,
                    no_check: bool = False, **kwargs
                    ) -> NEISOpenAPIData:
        """
        Fetches NEIS API data.

        :param name: School or Academy name.
        :param key: The API key used to authenticate the request.
        :param region: The region of the school or academy.
        :param no_check: Whether to perform code check.
        :param kwargs: Additional parameters for fetching data.
        :return: Fetched data from NEIS API.
        """
        if not no_check:
            identifiers = await CoAPIFetch.get_school_id(key, name, region)
        else:
            identifiers = ((name, region),)
        c, r = identifiers[0]
        _info, _meal, _schedule, _classroom = await gather(
            CoAPIFetch.fetch_school_info(key, c, r),
            CoAPIFetch.fetch_meal(
                key, c, r, **kwargs.get("meal", {})),
            CoAPIFetch.fetch_schedule(
                key, c, r, **kwargs.get("schedule", {})),
            CoAPIFetch.fetch_class(
                key, c, r, **kwargs.get("classroom", {}))
        )
        return SchoolData(
            info=_info,
            meal=_meal,
            schedule=_schedule,
            classroom=_classroom
        )

    @classmethod
    async def fetch_all(cls, name: str, key: str = "",
                        region: Region = Region.UNSPECIFIED, **kwargs
                        ) -> Tuple[NEISOpenAPIData, ...]:
        """
        Fetches NEIS API data for all schools or academies.

        :param name: School or Academy name.
        :param key: The API key used to authenticate the request.
        :param region: The region of the school or academy.
        :param kwargs: Additional parameters for fetching data.
        :return: Fetched data from NEIS API.
        """
        identifiers = await CoAPIFetch.get_school_id(key, name, region)
        tasks = []
        for c, r in identifiers:
            task = cls.fetch(c, key, r, no_check=True, **kwargs)
            tasks.append(task)
        return await gather(*tasks)
