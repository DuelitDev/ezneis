# ezneis
`ezneis`는 [NEIS Open API](https://open.neis.go.kr/)를 쉽게 사용할 수 있도록 도와주는 라이브러리입니다.

---
# 설치
```shell
pip install -U ezneis
```
---
# 핵심 기능
- 동기, 비동기(`asyncio`) 모두 지원
- 모든 데이터를 알맞은 자료형으로 변환 (파싱 지원)
- 지연된 불러오기(`lazy loading`) 구현
---
# 시작하기
```python
# 동기 방식 사용 예제
import ezneis


# API 키. 나이스 교육정보 개방 포털에서 발급받을 수 있습니다.
# 나이스 교육정보 개방 포털: https://open.neis.go.kr/
KEY = "your_api_key"

# 계성초등학교의 데이터 가져오기
data = ezneis.get_school(KEY, "계성초")
# 학교 기본 정보에서 학교명 출력
print("교명:", data.info.name)
# 학사 일정에서 오늘 자 6학년이 포함되는 일정 출력
print("금일 6학년 학사일정:", data.schedules.today.grade6)
# 급식 식단 정보에서 오늘 자 중식 출력
print("금일 중식:", data.meals.today.lunches)

# '서울'이 포함된 학교 중 3개의 학교 데이터 가져오기
data = ezneis.get_schools(KEY, "서울", hint=3)
...
```
```python
# 비동기 방식 사용 예제
import asyncio
import ezneis


# API 키. 나이스 교육정보 개방 포털에서 발급받을 수 있습니다.
# 나이스 교육정보 개방 포털: https://open.neis.go.kr/
KEY = "your_api_key"


async def main():
    # 계성초등학교의 데이터 가져오기
    data = await ezneis.get_school_async(KEY, "계성초")
    # 학교 기본 정보에서 학교명 출력
    print("교명:", (await data.info).name)
    # 학사 일정에서 오늘 자 6학년이 포함되는 일정 출력
    print("금일 6학년 학사일정:", (await data.schedules).today.grade6)
    # 급식 식단 정보에서 오늘 자 중식 출력
    print("금일 중식:", (await data.meals).today.lunches)

    # '서울'이 포함된 학교 중 3개의 학교 데이터 가져오기
    data = await ezneis.get_schools(KEY, "서울", hint=3)
    ...


asyncio.run(main())
```
---
# 자세한 사용 방법
[위키](https://github.com/DuelitDev/ezneis/wiki)를 참고하시기 바랍니다.

---
# 종속성
- [aiohttp](https://pypi.org/project/aiohttp/)
- [requests](https://pypi.org/project/requests/)

선택적으로 [aiodns](https://pypi.org/project/aiodns/) 라이브러리를 설치할 수 있습니다
(속도 향상을 위해 적극 권장됨, aiohttp README에서 발췌).
---
# 비슷한 프로젝트
- [neispy](https://pypi.org/project/neispy/)
  - 이 라이브러리는 `neispy`에서 영감을 받았습니다.
---
# 라이선스
`ezneis`는 MIT 라이선스 하에 제공됩니다.
