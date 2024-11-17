# -*- coding: utf-8 -*-
from collections import OrderedDict
from functools import wraps
from inspect import iscoroutinefunction
from time import time

__all__ = [
    "ttl_cache"
]


def deep_freeze(value):
    if isinstance(value, dict):
        return tuple((key, deep_freeze(val)) for key, val in value.items())
    elif isinstance(value, (list, set)):
        return tuple(deep_freeze(x) for x in value)
    return value


def ttl_cache(ttl: int, maxsize: int = 64):
    def decorator(func):
        nonlocal ttl
        cache = OrderedDict()

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            nonlocal ttl
            t_args = deep_freeze([args, kwargs])
            # cache disabled
            if ttl == 0:
                return func(*args, **kwargs)
            # get current time
            current = time()
            # clearing expired cache
            keys = [k for k, (_, t) in cache.items() if current - t > ttl]
            for key in keys:
                del cache[key]
            # check cache hit
            if t_args in cache:
                result, timestamp = cache.pop(t_args)
                if current - timestamp < ttl:
                    cache[t_args] = (result, timestamp)
                    return result
            # get a new result
            result = func(*args, **kwargs)
            cache[t_args] = (result, current)
            # remove old cache
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            nonlocal ttl
            t_args = deep_freeze([args, kwargs])
            # cache disabled
            if ttl == 0:
                return await func(*args, **kwargs)
            # get current time
            current = time()
            # clearing expired cache
            keys = [k for k, (_, t) in cache.items() if current - t > ttl]
            for key in keys:
                del cache[key]
            # check cache hit
            if t_args in cache:
                result, timestamp = cache.pop(t_args)
                if current - timestamp < ttl:
                    cache[t_args] = (result, timestamp)
                    return result
            # get a new result
            result = await func(*args, **kwargs)
            cache[t_args] = (result, current)
            # remove old cache
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        if iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper

    return decorator
