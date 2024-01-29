from django.core.cache import cache
import hashlib
import json
from functools import wraps


def make_cache_key(func, *args, **kwargs):
    key_parts = [func.__name__]
    for arg in args:
        key_parts.append(str(arg))
    for k, v in kwargs.items():
        key_parts.append(f"{k}={v}")
    hashed_key = hashlib.sha256("".join(key_parts).encode()).hexdigest()
    return f"cache:{hashed_key}"


def cache_response(timeout=60 * 5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # cache.set('test_key', 'test_value', timeout=60)
            # cached_value = cache.get('test_key')
            # print(cached_value)  # Powinno wyświetlić 'test_value'

            cache_key = make_cache_key(func, *args, **kwargs) # creates an unique key for function call 
            cached_result = cache.get(cache_key) # checking whether this function call is already stored in cache, and returns it if it is 
            if cached_result is not None:
                return cached_result
            result = func(*args, **kwargs) # if its not stored, we return the function with its arguments 
            cache.set(cache_key, result, timeout) # and store the response in local cache
            return result
        return wrapper
    return decorator