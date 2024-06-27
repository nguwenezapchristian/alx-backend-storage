#!/usr/bin/python3
""" Writing strings to Redis with Python """
from typing import List, Union
import redis
import uuid


class Cache:
    """ Class Cache """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: List[Union[str, int, float, bytes]]) -> str:
        """ Store data in Redis """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
