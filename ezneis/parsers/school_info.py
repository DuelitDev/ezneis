# -*- coding: utf-8 -*-
from datetime import datetime
from .common import Parser
from ..models.school_info import *
from ..utils.region import Region


class SchoolInfoParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> SchoolInfo:
        code = data["SD_SCHUL_CODE"]
        name = data["SCHUL_NM"]
        english_name = data["ENG_SCHUL_NM"]
        match data["FOND_SC_NM"]:
            case "공립": foundation_type = FoundationType.PUBLIC
            case "사립": foundation_type = FoundationType.PRIVATE
            case _:      foundation_type = FoundationType.UNSPECIFIED
        match data["SCHUL_KND_SC_NM"]:
            case "초등학교":         school_category = SchoolCategory.ELEMENTARY
            case "중학교":           school_category = SchoolCategory.MIDDLE
            case "고등학교":         school_category = SchoolCategory.HIGH
            case "특수학교":         school_category = SchoolCategory.SPECIAL
            case "방송통신고등학교": school_category = SchoolCategory.SEC_HIGH
            case "방송통신중학교":   school_category = SchoolCategory.SEC_MID
            case "각종학교(고)":     school_category = SchoolCategory.MISC_HIGH
            case "각종학교(중)":     school_category = SchoolCategory.MISC_MID
            case "각종학교(초)":     school_category = SchoolCategory.MISC_ELE
            case _:                  school_category = SchoolCategory.OTHERS
        match data["HS_GNRL_BUSNS_SC_NM"]:
            case "일반계": high_school_category = HighSchoolCategory.NORMAL
            case "전문계": high_school_category = HighSchoolCategory.VOCATIONAL
            case _:        high_school_category = None
        match data["HS_SC_NM"]:
            case None | "  ": subtype = None
            case "일반고":    subtype = HighSchoolSubtype.NORMAL
            case "특성화고":  subtype = HighSchoolSubtype.SPECIALIZED
            case "특목고":    subtype = HighSchoolSubtype.SPECIAL_PURPOSE
            case "자율고":    subtype = HighSchoolSubtype.AUTONOMOUS
            case _:           subtype = HighSchoolSubtype.OTHERS
        match data["SPCLY_PURPS_HS_ORD_NM"]:
            case None:         purpose = None
            case "국제계열":   purpose = SchoolPurpose.INTERNATIONAL
            case "체육계열":   purpose = SchoolPurpose.PHYSICAL
            case "예술계열":   purpose = SchoolPurpose.ART
            case "과학계열":   purpose = SchoolPurpose.SCIENCE
            case "외국어계열": purpose = SchoolPurpose.LANGUAGE
            case _:            purpose = SchoolPurpose.INDUSTRY
        match data["DGHT_SC_NM"]:
            case "주간": timing = SchoolTiming.DAY
            case "야간": timing = SchoolTiming.NIGHT
            case _:      timing = SchoolTiming.BOTH
        match data["ENE_BFE_SEHF_SC_NM"]:
            case "전기": admission_period = AdmissionPeriod.EARLY
            case "후기": admission_period = AdmissionPeriod.LATE
            case _:      admission_period = AdmissionPeriod.BOTH
        match data["COEDU_SC_NM"]:
            case "남여공학": gender_composition = GenderComposition.MIXED
            case "남":       gender_composition = GenderComposition.BOYS_ONLY
            case _:          gender_composition = GenderComposition.GIRLS_ONLY
        industry_supports = data["INDST_SPECL_CCCCL_EXST_YN"] == "Y"
        region            = Region(data["ATPT_OFCDC_SC_CODE"])
        address           = data["ORG_RDNMA"]
        address_detail    = data["ORG_RDNDA"]
        zip_code          = int(zc) if (zc := data["ORG_RDNZC"]) else -1
        jurisdiction_name = data["JU_ORG_NM"]
        tel_number        = data["ORG_TELNO"]
        fax_number        = data["ORG_FAXNO"]
        website           = data["HMPG_ADRES"]
        founded_date      = datetime.strptime(
                                data["FOND_YMD"], "%Y%m%d").date()
        anniversary       = datetime.strptime(
                                data["FOAS_MEMRD"], "%Y%m%d").date()
        return SchoolInfo(
            code=code,
            name=name,
            english_name=english_name,
            foundation_type=foundation_type,
            school_category=school_category,
            high_school_category=high_school_category,
            subtype=subtype,
            purpose=purpose,
            timing=timing,
            admission_period=admission_period,
            gender_composition=gender_composition,
            industry_supports=industry_supports,
            region=region,
            address=address,
            address_detail=address_detail,
            zip_code=zip_code,
            jurisdiction_name=jurisdiction_name,
            tel_number=tel_number,
            fax_number=fax_number,
            website=website,
            founded_date=founded_date,
            anniversary=anniversary,
        )
