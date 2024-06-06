from ezneis.util import *
from ezneis.types import *
from ezneis.parser import *
from ezneis.exception import *
from neispy import Neispy
from typing import Tuple
import neispy.error as ne

__all__ = [
    "SyncAPIFetch",
    "CoAPIFetch"
]

DEFAULT_LIMIT = 100
_USED_API = None


def _get_sync_api(*args, **kwargs):
    """
    :return: the instance of SyncNeispy that is currently being used.
             If no instance exists, a new instance of SyncNeispy will be created
             using the provided arguments and stored for future use.
    """
    global _USED_API
    if not _USED_API:
        _USED_API = Neispy.sync(*args, **kwargs)
    return _USED_API


class SyncAPIFetch:
    """
    A utility class for fetching various types of information
    from a school API synchronously.
    """

    @staticmethod
    def get_school_id(key: str, name: str, region: Region
                      ) -> Tuple[Tuple[str, Region], ...]:
        """
        Fetches the school code from school name.
        Or it can be used to check if the code is valid.

        :param name: School name or code.
        :param key: The API key used to authenticate the request.
        :param region: The region of the school.
        :return: Tuple of school codes.
        """
        api = _get_sync_api(KEY=key, pSize=DEFAULT_LIMIT)
        try:
            data = api.schoolInfo(SD_SCHUL_CODE=name)
        except ne.DataNotFound:
            try:
                data = api.schoolInfo(SCHUL_NM=name)
            except ne.DataNotFound:
                raise SchoolNotExistException
        return tuple((row.SD_SCHUL_CODE, Region(row.ATPT_OFCDC_SC_CODE))
                     for row in data.schoolInfo[1].row
                     if (region == Region.UNSPECIFIED or
                         row.ATPT_OFCDC_SC_CODE == region.value))

    @staticmethod
    def fetch_school_info(key: str, code: str, region: Region
                          ) -> SchoolInfo:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :return: An instance of `SchoolInfo`.
        """
        api = _get_sync_api(KEY=key, pSize=1)
        data = api.schoolInfo(
            SD_SCHUL_CODE=code,
            ATPT_OFCDC_SC_CODE=region.value)
        return SchoolInfoParser.parse(data)

    @staticmethod
    def fetch_meal(key: str, code: str, region: Region,
                   limit: int = DEFAULT_LIMIT, datetime: str = None,
                   ) -> Tuple[Meal, ...]:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :param limit: The maximum number of meals to fetch.
        :param datetime: The date in '[YYYY[MM[DD]]]' format to fetch meals for.
        :return: A tuple of `Meal` parsed from the API response.
        """
        if not datetime:
            datetime = _today_ymd_str()
        api = _get_sync_api(KEY=key, pSize=limit)
        try:
            data = api.mealServiceDietInfo(
                SD_SCHUL_CODE=code,
                ATPT_OFCDC_SC_CODE=region.value,
                MLSV_YMD=datetime)
        except ne.DataNotFound:
            return ()
        return SchoolMealParser.parse(data)

    @staticmethod
    def fetch_schedule(key: str, code: str, region: Region,
                       limit: int = DEFAULT_LIMIT, datetime: str = None,
                       ) -> Tuple[SchoolSchedule, ...]:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :param limit: The maximum number of meals to fetch.
        :param datetime: The date in '[YYYY[MM[DD]]]' format
                         to fetch schedules for.
        :return: A tuple of `SchoolSchedule` parsed from the API response.
        """
        if not datetime:
            datetime = _today_ym_str()
        api = _get_sync_api(KEY=key, pSize=limit)
        try:
            data = api.SchoolSchedule(
                SD_SCHUL_CODE=code,
                ATPT_OFCDC_SC_CODE=region.value,
                AA_YMD=datetime)
        except ne.DataNotFound:
            return ()
        return SchoolScheduleParser.parse(data)

    @staticmethod
    def fetch_class(key: str, code: str, region: Region,
                    limit: int = DEFAULT_LIMIT, datetime: str = None,
                    ) -> Classroom:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :param limit: The maximum number of meals to fetch.
        :param datetime: The date in '[YYYY[MM[DD]]]' format
                         to fetch class info for.
        :return: An instance of `Classroom` parsed from the API response.
        """
        if not datetime:
            datetime = _today_y_str()
        api = _get_sync_api(KEY=key, pSize=limit)
        try:
            data = api.classInfo(
                SD_SCHUL_CODE=code,
                ATPT_OFCDC_SC_CODE=region.value,
                AY=datetime)
        except ne.DataNotFound:
            return Classroom(())
        return ClassParser.parse(data)


class CoAPIFetch:
    """
    A utility class for fetching various types of information
    from a school API asynchronously.
    """

    @staticmethod
    async def get_school_id(key: str, name: str, region: Region
                            ) -> Tuple[Tuple[str, Region], ...]:
        """
        Fetches the school code from school name.
        Or it can be used to check if the code is valid.

        :param name: School name or code.
        :param key: The API key used to authenticate the request.
        :param region: The region of the school.
        :return: Tuple of school codes.
        """
        api = Neispy(KEY=key, pSize=DEFAULT_LIMIT)
        try:
            data = await api.schoolInfo(SD_SCHUL_CODE=name)
        except ne.DataNotFound:
            try:
                data = await api.schoolInfo(SCHUL_NM=name)
            except ne.DataNotFound:
                raise SchoolNotExistException
        await api.session.close()
        return tuple((row.SD_SCHUL_CODE, Region(row.ATPT_OFCDC_SC_CODE))
                     for row in data.schoolInfo[1].row
                     if (region == Region.UNSPECIFIED or
                         row.ATPT_OFCDC_SC_CODE == region.value))

    @staticmethod
    async def fetch_school_info(key: str, code: str, region: Region
                                ) -> SchoolInfo:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :return: An instance of `SchoolInfo`.
        """
        api = Neispy(KEY=key, pSize=1)
        data = await api.schoolInfo(
            SD_SCHUL_CODE=code,
            ATPT_OFCDC_SC_CODE=region.value)
        await api.session.close()
        return SchoolInfoParser.parse(data)

    @staticmethod
    async def fetch_meal(key: str, code: str, region: Region,
                         limit: int = DEFAULT_LIMIT, datetime: str = None,
                         ) -> Tuple[Meal, ...]:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :param limit: The maximum number of meals to fetch.
        :param datetime: The date in '[YYYY[MM[DD]]]' format to fetch meals for.
        :return: A tuple of `Meal` parsed from the API response.
        """
        if not datetime:
            datetime = _today_ymd_str()
        api = Neispy(KEY=key, pSize=limit)
        try:
            data = await api.mealServiceDietInfo(
                SD_SCHUL_CODE=code,
                ATPT_OFCDC_SC_CODE=region.value,
                MLSV_YMD=datetime)
        except ne.DataNotFound:
            return ()
        finally:
            await api.session.close()
        return SchoolMealParser.parse(data)

    @staticmethod
    async def fetch_schedule(key: str, code: str, region: Region,
                             limit: int = DEFAULT_LIMIT, datetime: str = None,
                             ) -> Tuple[SchoolSchedule, ...]:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :param limit: The maximum number of meals to fetch.
        :param datetime: The date in '[YYYY[MM[DD]]]' format
                         to fetch schedules for.
        :return: A tuple of `SchoolSchedule` parsed from the API response.
        """
        if not datetime:
            datetime = _today_ym_str()
        api = Neispy(KEY=key, pSize=limit)
        try:
            data = await api.SchoolSchedule(
                SD_SCHUL_CODE=code,
                ATPT_OFCDC_SC_CODE=region.value,
                AA_YMD=datetime)
        except ne.DataNotFound:
            return ()
        finally:
            await api.session.close()
        return SchoolScheduleParser.parse(data)

    @staticmethod
    async def fetch_class(key: str, code: str, region: Region,
                          limit: int = DEFAULT_LIMIT, datetime: str = None,
                          ) -> Classroom:
        """
        :param key: The API key used to authenticate the request.
        :param code: The code of the school to fetch information for.
        :param region: The region of the school.
        :param limit: The maximum number of meals to fetch.
        :param datetime: The date in '[YYYY[MM[DD]]]' format
                         to fetch class info for.
        :return: An instance of `Classroom` parsed from the API response.
        """
        if not datetime:
            datetime = _today_y_str()
        api = Neispy(KEY=key, pSize=limit)
        try:
            data = await api.classInfo(
                SD_SCHUL_CODE=code,
                ATPT_OFCDC_SC_CODE=region.value,
                AY=datetime)
        except ne.DataNotFound:
            return Classroom(())
        finally:
            await api.session.close()
        return ClassParser.parse(data)
