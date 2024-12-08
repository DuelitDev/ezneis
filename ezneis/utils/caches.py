# -*- coding: utf-8 -*-
from collections import OrderedDict
from functools import wraps, lru_cache
from inspect import iscoroutinefunction
from time import time
from weakref import ref

__all__ = [
    "ttl_cache"
]


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
def lru_cache_instance(maxsize=128, typed=False):
    """
    LRU 알고리즘에 기반하여 인스턴스 단위의 캐시를 구현한 데코레이터입니다.

    functools의 lru_cache와 동일하게 동작합니다.

    :param maxsize:
    :param typed:
    :return: LRU 캐시 데코레이터.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self_weak = ref(self)

            @wraps(func)
            @lru_cache(maxsize=maxsize, typed=typed)
            def cached_method(*args2, **kwargs2):
                return func(self_weak(), *args2, **kwargs2)

            setattr(self, func.__name__, cached_method)
            return cached_method(*args, **kwargs)
        return wrapper
    return decorator


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
def _deep_freeze(value: dict | list | set):
    """
    입력 값을 재귀적으로 해시 가능한 형태로 변환합니다.

    변경 가능한(mutable) 자료형들을 재귀적으로 순회, 모두 튜플로 변환하여
    변경 불가능한 상태(immutable)로 만듭니다.

    :param value: 해시 가능한 형태로 변환할 입력 값.
    :return: 해시 가능한 형태로 변환된 입력 값.
    """
    if isinstance(value, dict):
        return frozenset((key, _deep_freeze(val)) for key, val in value.items())
    elif isinstance(value, (list, set)):
        return frozenset(_deep_freeze(x) for x in value)
    return value


# noinspection SpellCheckingInspection
# noinspection GrazieInspection
# PyCharm IDE의 오탈자/문법 관련 기능을 무시
def ttl_cache(ttl: int, maxsize: int = 64, is_method: bool = False):
    """
    TTL(Time-To-Live) 캐시를 구현한 데코레이터입니다.

    함수의 반환 값을 캐싱하여 설정된 기간 동안 재사용하며, 설정된 기간이 지난 후
    다음 호출 시 자동으로 삭제됩니다.

    또한, 최대 캐시 크기를 설정하여 메모리 사용을 제한할 수 있습니다.

    마지막으로, 클래스의 메소드인 경우 args의 첫번째를 생략합니다.

    이 데코레이터는 동기 및 비동기 함수 모두에 사용할 수 있습니다.

    :param ttl: 캐시의 유효 기간(초), 0일 경우 캐싱이 비활성화됩니다.
    :param maxsize: 캐시가 저장될 최대 스택 크기.
    :param is_method: 데코레이팅하는 함수가 클래스의 메소드인지 여부.
    :return: Time-To-Live 캐시 데코레이터.
    """
    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            # 파라미터를 키로 사용하기 위해 해시 가능하도록 변환
            if is_method:
                # 클래스 메소드인 경우 args 첫번째 생략
                t_args = _deep_freeze([args[1:], kwargs])
            else:
                t_args = _deep_freeze([args, kwargs])
            # 캐시가 비활성화된 경우, 함수 실행 및 결과 반환
            if ttl == 0:
                return func(*args, **kwargs)
            # 현재 시간 저장
            current = time()
            # 만료된 캐시 삭제
            keys = [k for k, (_, t) in cache.items() if current - t > ttl]
            for key in keys:
                del cache[key]
            # 캐시 히트 검사
            if t_args in cache:
                result, timestamp = cache.pop(t_args)
                if current - timestamp < ttl:
                    cache[t_args] = (result, timestamp)
                    return result
            # 캐시 히트에 실패한 경우, 함수 실행
            result = func(*args, **kwargs)
            cache[t_args] = (result, current)
            # 스택이 가득찬 경우, 가장 오래된 캐시 삭제
            if len(cache) > maxsize:
                cache.popitem(last=False)
            # 결과 반환
            return result

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            nonlocal ttl
            # 파라미터를 키로 사용하기 위해 해시 가능하도록 변환
            t_args = _deep_freeze([args, kwargs])
            # 캐시가 비활성화된 경우, 함수 실행 및 결과 반환
            if ttl == 0:
                return await func(*args, **kwargs)
            # 현재 시간 저장
            current = time()
            # 만료된 캐시 삭제
            keys = [k for k, (_, t) in cache.items() if current - t > ttl]
            for key in keys:
                del cache[key]
            # 캐시 히트 검사
            if t_args in cache:
                result, timestamp = cache.pop(t_args)
                if current - timestamp < ttl:
                    cache[t_args] = (result, timestamp)
                    return result
            # 캐시 히트에 실패한 경우, 함수 실행
            result = await func(*args, **kwargs)
            cache[t_args] = (result, current)
            # 스택이 가득찬 경우, 가장 오래된 캐시 삭제
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        if iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper

    return decorator
