#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps
"""
Exercise
Write a Redis client that counts the number of calls to a particular method
"""


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of calls to a method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Construct the key for the method call count """
        key = f"{method.__qualname__}_calls"
        """ Increment the count in Redis """
        self._redis.incr(key)
        """ Call the original method """
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)
