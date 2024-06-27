#!/usr/bin/env python3
""" Writing strings to Redis with Python """
from typing import Union
import redis
import uuid


class Cache:
    """ Class Cache """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: callable = None) -> Union[str,
                                                          bytes,
                                                          int,
                                                          float]:
        """ Get data from Redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """ Get string from Redis """
        return self.get(key, str)
    
    def get_int(self, key: str) -> int:
        """ Get int from Redis """
        return self.get(key, int)