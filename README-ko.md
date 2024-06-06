# ezneis


# 다른 언어
- 한국어 (이 문서)  
- [English](https://github.com/DuelitDev/ezneis/blob/main/README.md)


# 설명
`ezneis`는 [나이스 Open API](https://open.neis.go.kr/)를 쉽게 사용할 수 있도록 도와주는 라이브러리입니다.  
동기, 비동기 모두 지원하며 모든 데이터가 파싱되어 간단하게 데이터를 이용할 수 있습니다.


# 설치 및 업데이트
```shell
# 설치
pip install ezneis

# 업데이트
pip install --upgrade ezneis
```


# 사용 예시
```python
# example.py
import ezneis


# ----- 간단한 사용 예시 -----

sc1 = ezneis.fetch("계성초")
print("교명:", sc1.info.name)

sc2 = ezneis.fetch_all("고등학교")
for s in sc2:
    print("교명:", s.info.name)


# ----- 고급 사용 예시 -----

# `ezneis.fetch_all`도 동일하게 사용 가능합니다.
sc3 = ezneis.fetch(
    name="계성초등학교",  # 학교나 학원의 이름 또는 코드
    key="YOUR_API_KEY",  # 나이스 API 키, 지정되지 않을 경우 샘플키로 요청합니다.
    region=ezneis.R_SEOUL,  # 학교나 학원이 위치한 지역, 지정되지 않을 경우 전국을 대상으로 합니다.
    meal={  # 급식 데이터 인출 설정입니다.
        "limit": 3,  # 급식 데이터를 최대 3개까지 가져옵니다. (기본값은 100)
        "datetime": "20240501"  # 2024년 5월 1일의 급식을 가져옵니다.
        # "datetime": "202405"  # 2024년 5월 간의 급식을 가져옵니다.
        # "datetime": "2024"    # 2024년 간의 급식을 가져옵니다.
    },
    schedule={
        "limit": 5,  # 일정 데이터를 최대 5개까지 가져옵니다. (기본값은 100)
        "datetime": "20240501"  # 2024년 5월 1일의 일정을 가져옵니다.
        # "datetime": "202405"  # 2024년 5월 간의 일정을 가져옵니다.
        # "datetime": "2024"    # 2024년 간의 일정을 가져옵니다.
    },
    classroom={
        "limit": 30,  # 학급 데이터를 최대 30개까지 가져옵니다. (기본값은 100)
        "datetime": "2024"  # 2024년의 학급 데이터를 가져옵니다.
    }
)
print("교명:", sc3.info.name)
print()
print("급식:", sc3.meal)
print()
print("학사일정:", sc3.schedule)
print()
print("1학년 학급:", sc3.classroom.grade1)
```
```python
# example_async.py
import asyncio
import ezneis


async def main():
    # ----- 간단한 사용 예시 -----
    
    sc1 = await ezneis.fetch_async("계성초")
    print("교명:", sc1.info.name)
    
    sc2 = await ezneis.fetch_all_async("고등학교")
    for s in sc2:
        print("교명:", s.info.name)


    # ----- 고급 사용 예시 -----
    
    # `ezneis.fetch_all_async`도 동일하게 사용 가능합니다.
    sc3 = await ezneis.fetch_async(
        name="계성초등학교",  # 학교나 학원의 이름 또는 코드
        key="YOUR_API_KEY",  # 나이스 API 키, 지정되지 않을 경우 샘플키로 요청합니다.
        region=ezneis.R_SEOUL,  # 학교나 학원이 위치한 지역, 지정되지 않을 경우 전국을 대상으로 합니다.
        meal={  # 급식 데이터 인출 설정입니다.
            "limit": 3,  # 급식 데이터를 최대 3개까지 가져옵니다. (기본값은 100)
            "datetime": "20240501"  # 2024년 5월 1일의 급식을 가져옵니다.
            # "datetime": "202405"  # 2024년 5월 간의 급식을 가져옵니다.
            # "datetime": "2024"    # 2024년 간의 급식을 가져옵니다.
        },
        schedule={
            "limit": 5,  # 일정 데이터를 최대 5개까지 가져옵니다. (기본값은 100)
            "datetime": "20240501"  # 2024년 5월 1일의 일정을 가져옵니다.
            # "datetime": "202405"  # 2024년 5월 간의 일정을 가져옵니다.
            # "datetime": "2024"    # 2024년 간의 일정을 가져옵니다.
        },
        classroom={
            "limit": 30,  # 학급 데이터를 최대 30개까지 가져옵니다. (기본값은 100)
            "datetime": "2024"  # 2024년의 학급 데이터를 가져옵니다.
        }
    )
    print("교명:", sc3.info.name)
    print()
    print("급식:", sc3.meal)
    print()
    print("학사일정:", sc3.schedule)
    print()
    print("1학년 학급:", sc3.classroom.grade1)


asyncio.run(main())
```
더 자세한 정보는 [위키](https://github.com/DuelitDev/ezneis/wiki)를 참고하시기 바랍니다.
