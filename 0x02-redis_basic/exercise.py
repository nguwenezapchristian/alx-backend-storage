import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps
""" Exercise """

def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of calls to a method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}_calls"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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


def replay(method: Callable):
    """
    Function to display the history of calls of a particular function.
    """
    r = redis.Redis()

    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = r.lrange(input_key, 0, -1)
    outputs = r.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for inp, outp in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")
