from ezneis.parser.core import *
from ezneis.types.school.classroom import *
from uuid import uuid4

__all__ = [
    "ClassParser"
]


class ClassParser(Parser):
    """
    A parser class to extract class information from provided data.
    """

    @classmethod
    def parse(cls, data) -> Classroom:
        """
        Parse the class information from the given data.

        :param data: The data to parse the class information from.
        :return: The parsed class information.
        """
        data = tuple(cls._run_parsers(row) for row
                     in data.classInfo[1].row)
        return Classroom(data)

    @staticmethod
    def _parser1(r) -> ClassInfo:
        """
        :param r: The object containing class information.
        :return: An instance of the `ClassInfo` class.
        """
        year       = int(r.AY)
        grade      = int(r.GRADE)
        name       = r.CLASS_NM if r.CLASS_NM else uuid4().urn[9:]
        department = r.DDDEP_NM
        course = (
            ClassCourse.PRESCHOOL  if r.SCHUL_CRSE_SC_NM == "유치원" else
            ClassCourse.ELEMENTARY if r.SCHUL_CRSE_SC_NM == "초등학교" else
            ClassCourse.MIDDLE     if r.SCHUL_CRSE_SC_NM == "중학교" else
            ClassCourse.HIGH       if r.SCHUL_CRSE_SC_NM == "고등학교" else
            ClassCourse.SPECIALITY
        )
        course_detail = (
            ClassDetailCourse.NORMAL        if r.ORD_SC_NM == "일반계" else
            ClassDetailCourse.VOCATIONAL    if r.ORD_SC_NM == "전문계" else
            ClassDetailCourse.SPECIALIZED   if r.ORD_SC_NM == "특성화" else
            ClassDetailCourse.INTERNATIONAL if r.ORD_SC_NM == "국제계" else
            ClassDetailCourse.BUSINESS      if r.ORD_SC_NM in ("가사실업계열",
                                                               "가사실업계",
                                                               "가사계") else
            ClassDetailCourse.COMMERCE      if r.ORD_SC_NM in ("전자미디어계",
                                                               "상업정보계열",
                                                               "상업계",
                                                               "직업") else
            ClassDetailCourse.TECHNICAL     if r.ORD_SC_NM in ("공업계열",
                                                               "공업계") else
            ClassDetailCourse.AGRICULTURE   if r.ORD_SC_NM in ("도시형첨단농업경영계열",
                                                               "농생명산업계열",
                                                               "농생명계",
                                                               "농업계") else
            ClassDetailCourse.FISHERIES     if r.ORD_SC_NM == "수산해양계" else
            ClassDetailCourse.INTEGRATED    if r.ORD_SC_NM == "통합계" else
            ClassDetailCourse.LANGUAGE      if r.ORD_SC_NM == "외국어계" else
            ClassDetailCourse.SCIENCE       if r.ORD_SC_NM == "과학계" else
            ClassDetailCourse.PHYSICAL      if r.ORD_SC_NM == "체육계" else
            ClassDetailCourse.ART           if r.ORD_SC_NM == "예술계" else
            ClassDetailCourse.ALTERNATIVE   if r.ORD_SC_NM == "대안" else
            ClassDetailCourse.TRAINING      if r.ORD_SC_NM == "공동실습소" else
            ClassDetailCourse.NONE
        )
        part_time = (
            ClassTimeClassification.DAY   if r.DGHT_CRSE_SC_NM == "주간" else
            ClassTimeClassification.NIGHT if r.DGHT_CRSE_SC_NM == "야간" else
            ClassTimeClassification.NONE
        )
        return ClassInfo(
            year=year,
            grade=grade,
            name=name,
            department=department,
            course=course,
            course_detail=course_detail,
            time=part_time,
        )

    _parsers = (_parser1,)
