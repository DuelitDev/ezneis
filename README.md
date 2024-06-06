# ezneis


# Other languages
- English (here)  
- [한국어](https://github.com/DuelitDev/ezneis/blob/main/README-ko.md)


# Description
`ezneis` is a library that help to use easily the [NEIS Open API](https://open.neis.go.kr/).  
supports both sync and async, all data has been parsed, so it can be used easily.


# Install & Update
```shell
# Install
pip install ezneis

# Update
pip install --upgrade ezneis
```


# Example
```python
# example.py
import ezneis


# ----- Simple example -----

sc1 = ezneis.fetch("계성초")  # Gyeseong Elementary School
print("School name:", sc1.info.name)

sc2 = ezneis.fetch_all("고등학교")  # High School
for s in sc2:
    print("School name:", s.info.name)


# ----- Advanced example -----

# `ezneis.fetch_all` can also be used like this.
sc3 = ezneis.fetch(
    name="계성초등학교",  # Name or code of school or academy.
    key="YOUR_API_KEY",  # NEIS API key, if not specified, will be requested as a sample.
    region=ezneis.R_SEOUL,  # The region of the school or academy, or the entire country if not specified.
    meal={  # fetch options of meal data.
        "limit": 3,  # Fetch up to 3 data. (Default is 100)
        "datetime": "20240501"  # Fetch data for May 1st, 2024.
        # "datetime": "202405"  # Fetch data for May 2024.
        # "datetime": "2024"    # Fetch data for 2024.
    },
    schedule={
        "limit": 5,  # Fetch up to 5 data. (Default is 100)
        "datetime": "20240501"  # Fetch data for May 1st, 2024.
        # "datetime": "202405"  # Fetch data for May 2024.
        # "datetime": "2024"    # Fetch data for 2024.
    },
    classroom={
        "limit": 30,  # Fetch up to 30 data. (Default is 100)
        "datetime": "2024"  # Fetch data for 2024.
    }
)
print("School name:", sc3.info.name)
print()
print("Meals:", sc3.meal)
print()
print("Schedule:", sc3.schedule)
print()
print("Classes of 1st grade:", sc3.classroom.grade1)
```
```python
# example_async.py
import asyncio
import ezneis


async def main():
    # ----- Simple example -----
    
    sc1 = await ezneis.fetch_async("계성초")  # Gyeseong Elementary School
    print("School name:", sc1.info.name)
    
    sc2 = await ezneis.fetch_all_async("고등학교")  # High School
    for s in sc2:
        print("School name:", s.info.name)
    
    
    # ----- Advanced example -----
    
    # `ezneis.fetch_all` can also be used like this.
    sc3 = await ezneis.fetch_async(
        name="계성초등학교",  # Name or code of school or academy.
        key="YOUR_API_KEY",  # NEIS API key, if not specified, will be requested as a sample.
        region=ezneis.R_SEOUL,  # The region of the school or academy, or the entire country if not specified.
        meal={  # fetch options of meal data.
            "limit": 3,  # Fetch up to 3 data. (Default is 100)
            "datetime": "20240501"  # Fetch data for May 1st, 2024.
            # "datetime": "202405"  # Fetch data for May 2024.
            # "datetime": "2024"    # Fetch data for 2024.
        },
        schedule={
            "limit": 5,  # Fetch up to 5 data. (Default is 100)
            "datetime": "20240501"  # Fetch data for May 1st, 2024.
            # "datetime": "202405"  # Fetch data for May 2024.
            # "datetime": "2024"    # Fetch data for 2024.
        },
        classroom={
            "limit": 30,  # Fetch up to 30 data. (Default is 100)
            "datetime": "2024"  # Fetch data for 2024.
        }
    )
    print("School name:", sc3.info.name)
    print()
    print("Meals:", sc3.meal)
    print()
    print("Schedule:", sc3.schedule)
    print()
    print("Classes of 1st grade:", sc3.classroom.grade1)


asyncio.run(main())
```
For more information, please refer to the [wiki](https://github.com/DuelitDev/ezneis/wiki).

