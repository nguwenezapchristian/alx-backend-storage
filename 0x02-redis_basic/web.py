#!/usr/bin/env python3
import requests
import redis
from typing import Callable
from functools import wraps

""" Initialize Redis client """
r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Decorator to count the number of requests to a URL.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs) -> str:
        """ Increment the counter for the URL """
        r.incr(f"count:{url}")
        return method(url, *args, **kwargs)
    return wrapper


def cache_response(method: Callable) -> Callable:
    """
    Decorator to cache the response of a URL request.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs) -> str:
        """ Check if the URL is already cached """
        cached_response = r.get(f"cache:{url}")
        if cached_response:
            return cached_response.decode('utf-8')

        """ If not cached, call the original method """
        response = method(url, *args, **kwargs)

        """ Cache the response with an expiration time of 10 seconds """
        r.setex(f"cache:{url}", 10, response)
        return response
    return wrapper


@count_requests
@cache_response
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL.
    """
    response = requests.get(url)
    return response.text
