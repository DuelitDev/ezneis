from ezneis.api import *
from ezneis.util import *
from ezneis.types import *
from typing import Tuple

__all__ = [
    "R_UNSPECIFIED",
    "R_SEOUL",
    "R_BUSAN",
    "R_DAEGU",
    "R_INCHEON",
    "R_GWANGJU",
    "R_DAEJEON",
    "R_ULSAN",
    "R_SEJONG",
    "R_GYEONGGI",
    "R_GANGWON",
    "R_CHUNGBUK",
    "R_CHUNGNAM",
    "R_JEONBUK",
    "R_JEONNAM",
    "R_GYEONGBUK",
    "R_GYEONGNAM",
    "R_JEJU",
    "R_FOREIGNER",
    "fetch",
    "fetch_all"
]

# Regions
R_UNSPECIFIED = Region.UNSPECIFIED  # noqa
R_SEOUL       = Region.SEOUL        # noqa
R_BUSAN       = Region.BUSAN        # noqa
R_DAEGU       = Region.DAEGU        # noqa
R_INCHEON     = Region.INCHEON      # noqa
R_GWANGJU     = Region.GWANGJU      # noqa
R_DAEJEON     = Region.DAEJEON      # noqa
R_ULSAN       = Region.ULSAN        # noqa
R_SEJONG      = Region.SEJONG       # noqa
R_GYEONGGI    = Region.GYEONGGI     # noqa
R_GANGWON     = Region.GANGWON      # noqa
R_CHUNGBUK    = Region.CHUNGBUK     # noqa
R_CHUNGNAM    = Region.CHUNGNAM     # noqa
R_JEONBUK     = Region.JEONBUK      # noqa
R_JEONNAM     = Region.JEONNAM      # noqa
R_GYEONGBUK   = Region.GYEONGBUK    # noqa
R_GYEONGNAM   = Region.GYEONGNAM    # noqa
R_JEJU        = Region.JEJU         # noqa
R_FOREIGNER   = Region.FOREIGNER    # noqa

# default api instance
_default_co_api   = CoAPI()
_default_sync_api = SyncAPI()


def fetch(name: str, key: str = "",
          region: Region = Region.UNSPECIFIED, **kwargs
          ) -> NEISOpenAPIData:
    """
    :param name: School or Academy name.
    :param key: The API key used to authenticate the request.
    :param region: The region of the school or academy.
    :param kwargs: Additional parameters for fetching data.
    :return: Fetched data from NEIS API.
    """
    return _default_sync_api.fetch(name, key, region, **kwargs)


async def fetch_async(name: str, key: str = "",
                      region: Region = Region.UNSPECIFIED, **kwargs
                      ) -> NEISOpenAPIData:
    """
    :param name: School or Academy name.
    :param key: The API key used to authenticate the request.
    :param region: The region of the school or academy.
    :param kwargs: Additional parameters for fetching data.
    :return: Fetched data from NEIS API.
    """
    return await _default_co_api.fetch(name, key, region, **kwargs)


def fetch_all(name: str, key: str = "",
              region: Region = Region.UNSPECIFIED, **kwargs
              ) -> Tuple[NEISOpenAPIData, ...]:
    """
    :param name: School or Academy name.
    :param key: The API key used to authenticate the request.
    :param region: The region of the school or academy.
    :param kwargs: Additional parameters for fetching data.
    :return: Fetched data from NEIS API.
    """
    return _default_sync_api.fetch_all(name, key, region, **kwargs)


async def fetch_all_async(name: str, key: str = "",
                          region: Region = Region.UNSPECIFIED, **kwargs
                          ) -> Tuple[NEISOpenAPIData, ...]:
    """
    :param name: School or Academy name.
    :param key: The API key used to authenticate the request.
    :param region: The region of the school or academy.
    :param kwargs: Additional parameters for fetching data.
    :return: Fetched data from NEIS API.
    """
    return await _default_co_api.fetch_all(name, key, region, **kwargs)
