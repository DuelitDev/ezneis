# -*- coding: utf-8 -*-
from datetime import datetime
from .common import Parser
from ..models.school_info import *
from ..utils.region import Region

__all__ = [
    "SchoolInfoParser"
]


class SchoolInfoParser(Parser):
    @classmethod
    def from_json(cls, data: dict) -> SchoolInfo:
        # 시도 교육청 코드
        region = Region(data["ATPT_OFCDC_SC_CODE"])
        # 행정 표준 코드
        code = data["SD_SCHUL_CODE"]
        # 학교명
        name = data["SCHUL_NM"]
        # 영문 학교명
        english_name = data["ENG_SCHUL_NM"]
        # 학교 종류명
        school_category_name = data["SCHUL_KND_SC_NM"]
        # 학교 종류명
        match school_category_name:
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
        # 관할 조직명
        jurisdiction_name = data["JU_ORG_NM"]
        # 설립명
        match data["FOND_SC_NM"]:
            case "공립": foundation_type = FoundationType.PUBLIC
            case "사립": foundation_type = FoundationType.PRIVATE
            case "국립": foundation_type = FoundationType.NATIONAL
            case _:      foundation_type = FoundationType.OTHERS
        # 도로명 우편 번호
        zip_code = zc if (zc := data["ORG_RDNZC"]) is not None else None
        # 도로명 주소
        address = data["ORG_RDNMA"]
        # 도로명 상세 주소
        address_detail = data["ORG_RDNDA"]
        # 전화 번호
        tel_number = data["ORG_TELNO"]
        # 홈페이지 주소
        website = data["HMPG_ADRES"]
        # 남녀공학 구분명
        match data["COEDU_SC_NM"]:
            case "남여공학": gender_composition = GenderComposition.MIXED
            case "남":       gender_composition = GenderComposition.BOYS_ONLY
            case _:          gender_composition = GenderComposition.GIRLS_ONLY
        # 팩스 번호
        fax_number = data["ORG_FAXNO"]
        # 고등학교 구분명
        match data["HS_SC_NM"]:
            case None | "  ": subtype = None
            case "일반고":    subtype = HighSchoolSubtype.NORMAL
            case "특성화고":  subtype = HighSchoolSubtype.SPECIALIZED
            case "특목고":    subtype = HighSchoolSubtype.SPECIAL_PURPOSE
            case "자율고":    subtype = HighSchoolSubtype.AUTONOMOUS
            case _:           subtype = HighSchoolSubtype.OTHERS
        # 산업체 특별 학급 존재 여부
        industry_supports = data["INDST_SPECL_CCCCL_EXST_YN"] == "Y"
        # 고등학교 일반 전문 구분명
        match data["HS_GNRL_BUSNS_SC_NM"]:
            case "일반계": high_school_category = HighSchoolCategory.NORMAL
            case "전문계": high_school_category = HighSchoolCategory.VOCATIONAL
            case _:        high_school_category = None
        # 특수 목적 고등학교 계열명
        match data["SPCLY_PURPS_HS_ORD_NM"]:
            case None:         purpose = None
            case "국제계열":   purpose = SchoolPurpose.INTERNATIONAL
            case "체육계열":   purpose = SchoolPurpose.PHYSICAL
            case "예술계열":   purpose = SchoolPurpose.ART
            case "과학계열":   purpose = SchoolPurpose.SCIENCE
            case "외국어계열": purpose = SchoolPurpose.LANGUAGE
            case _:            purpose = SchoolPurpose.INDUSTRY
        # 입시 전후기 구분명
        match data["ENE_BFE_SEHF_SC_NM"]:
            case "전기": admission_period = AdmissionPeriod.EARLY
            case "후기": admission_period = AdmissionPeriod.LATE
            case _:      admission_period = AdmissionPeriod.BOTH
        # 주야 구분명
        match data["DGHT_SC_NM"]:
            case "주간": timing = Timing.DAY
            case "야간": timing = Timing.NIGHT
            case _:      timing = Timing.BOTH
        # 설립 일자
        founded_date = datetime.strptime(data["FOND_YMD"], "%Y%m%d").date()
        # 개교 기념일
        anniversary = datetime.strptime(data["FOAS_MEMRD"], "%Y%m%d").date()
        return SchoolInfo(
            region=region,
            code=code,
            name=name,
            english_name=english_name,
            school_category=school_category,
            jurisdiction_name=jurisdiction_name,
            foundation_type=foundation_type,
            zip_code=zip_code,
            address=address,
            address_detail=address_detail,
            tel_number=tel_number,
            website=website,
            gender_composition=gender_composition,
            fax_number=fax_number,
            subtype=subtype,
            industry_supports=industry_supports,
            high_school_category=high_school_category,
            purpose=purpose,
            admission_period=admission_period,
            timing=timing,
            founded_date=founded_date,
            anniversary=anniversary,
        )
