from datetime import datetime
from ezneis.parser.core import *
from ezneis.types.school.info import *
from ezneis.util import Region

__all__ = [
    "SchoolInfoParser"
]


class SchoolInfoParser(Parser):
    """
    A parser class to extract school information from provided data.
    """

    @classmethod
    def parse(cls, data) -> SchoolInfo:
        """
        Parse the school information from the given data.

        :param data: The data to parse the school information from.
        :return: The parsed school information.
        """
        return cls._run_parsers(data.schoolInfo[1].row[0])

    @staticmethod
    def _parser1(r) -> SchoolInfo:
        """
        :param r: The object containing school information.
        :return: An instance of the `SchoolInfo` class.
        """
        code = r.SD_SCHUL_CODE
        name = r.SCHUL_NM
        english_name = r.ENG_SCHUL_NM
        foundation = (
            Foundation.PUBLIC  if r.FOND_SC_NM == "공립" else
            Foundation.PRIVATE if r.FOND_SC_NM == "사립" else
            Foundation.UNSPECIFIED
        )
        types = ((
            SchoolType.SECONDARY_MID  if r.SCHUL_KND_SC_NM == "방송통신중학교" else
            SchoolType.SECONDARY_HIGH if r.SCHUL_KND_SC_NM == "방송통신고등학교" else
            SchoolType.MISC_ELE       if r.SCHUL_KND_SC_NM == "각종학교(초)" else
            SchoolType.MISC_MID       if r.SCHUL_KND_SC_NM == "각종학교(중)" else
            SchoolType.MISC_HIGH      if r.SCHUL_KND_SC_NM == "각종학교(고)" else
            SchoolType.SPECIAL        if r.SCHUL_KND_SC_NM == "특수학교" else
            SchoolType.ELEMENTARY     if r.SCHUL_KND_SC_NM == "초등학교" else
            SchoolType.MIDDLE         if r.SCHUL_KND_SC_NM == "중학교" else
            SchoolType.HIGH           if r.SCHUL_KND_SC_NM == "고등학교" else
            SchoolType.OTHERS
        ), (
            HighSchoolType.NORMAL     if r.HS_GNRL_BUSNS_SC_NM == "일반계" else
            HighSchoolType.VOCATIONAL if r.HS_GNRL_BUSNS_SC_NM == "전문계" else
            HighSchoolType.NONE
        ), (
            HighSchoolDetailType.NORMAL          if r.HS_SC_NM == "일반고" else
            HighSchoolDetailType.SPECIALIZED     if r.HS_SC_NM == "특성화고" else
            HighSchoolDetailType.SPECIAL_PURPOSE if r.HS_SC_NM == "특목고" else
            HighSchoolDetailType.AUTONOMOUS      if r.HS_SC_NM == "자율고" else
            HighSchoolDetailType.OTHERS          if r.HS_SC_NM == "99" else
            HighSchoolDetailType.NONE
        ), (
            Purpose.INTERNATIONAL if r.SPCLY_PURPS_HS_ORD_NM == "국제계열" else
            Purpose.PHYSICAL      if r.SPCLY_PURPS_HS_ORD_NM == "체육계열" else
            Purpose.ART           if r.SPCLY_PURPS_HS_ORD_NM == "예술계열" else
            Purpose.SCIENCE       if r.SPCLY_PURPS_HS_ORD_NM == "과학계열" else
            Purpose.LANGUAGE      if r.SPCLY_PURPS_HS_ORD_NM == "외국어계열" else
            Purpose.INDUSTRY      if r.SPCLY_PURPS_HS_ORD_NM is not None else
            Purpose.NONE
        ))
        part_time = (
            SchoolTimeClassification.DAY   if r.DGHT_SC_NM == "주간" else
            SchoolTimeClassification.NIGHT if r.DGHT_SC_NM == "야간" else
            SchoolTimeClassification.BOTH
        )
        entrance_period = (
            EntrancePeriod.EARLY if r.ENE_BFE_SEHF_SC_NM == "전기" else
            EntrancePeriod.LATER if r.ENE_BFE_SEHF_SC_NM == "후기" else
            EntrancePeriod.BOTH
        )
        students_sex = (
            StudentsSex.BOYS_ONLY  if r.COEDU_SC_NM == "남" else
            StudentsSex.GIRLS_ONLY if r.COEDU_SC_NM == "여" else
            StudentsSex.MIXED
        )
        industry_supports = r.INDST_SPECL_CCCCL_EXST_YN == 'Y'
        region            = Region(r.ATPT_OFCDC_SC_CODE)
        address           = r.ORG_RDNMA
        address_detail    = r.ORG_RDNDA
        zip_code          = int(r.ORG_RDNZC) if r.ORG_RDNZC else -1
        jurisdiction_name = r.JU_ORG_NM
        tel_number        = r.ORG_TELNO
        fax_number        = r.ORG_FAXNO
        website           = r.HMPG_ADRES
        found_date        = datetime.strptime(r.FOND_YMD,   "%Y%m%d").date()
        anniversary       = datetime.strptime(r.FOAS_MEMRD, "%Y%m%d").date()
        return SchoolInfo(
            code=code,
            name=name,
            english_name=english_name,
            foundation=foundation,
            types=types,
            time=part_time,
            entrance_period=entrance_period,
            students_sex=students_sex,
            industry_supports=industry_supports,
            region=region,
            address=address,
            address_detail=address_detail,
            zip_code=zip_code,
            jurisdiction_name=jurisdiction_name,
            tel_number=tel_number,
            fax_number=fax_number,
            website=website,
            found_date=found_date,
            anniversary=anniversary,
        )

    _parsers = (_parser1,)
