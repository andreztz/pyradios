import pickle
import time
from functools import wraps
from pathlib import Path

from appdirs import user_cache_dir


def setup_cache_file(filename, **kwargs):
    appname = kwargs.get("appname")
    appauthor = kwargs.get("appauthor")
    cache_dir = Path(user_cache_dir(appname=appname, appauthor=appauthor))
    if not cache_dir.exists():
        cache_dir.mkdir()
    cache_file = cache_dir / filename
    return cache_file


def write_file(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def read_file(filename):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return data
    except IOError as exc:
        print(exc)
    return {}


def read_cache(filename, key):

    data = read_file(filename)
    try:
        expiry, value = data[key]
    except KeyError:
        return
    if time.time() > expiry:
        del data[key]
        write_file(filename, data)
        return
    return value


def save_cache(filename, key, value, ttl):
    data = read_file(filename)
    expiry = time.time() + int(ttl)
    data[key] = (expiry, value)
    write_file(filename, data)


def cache(filename, ttl, **kwargs):

    filename = setup_cache_file(filename, **kwargs)

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not ttl:
                return func(*args, **kwargs)

            key = func.__name__
            cache_value = read_cache(filename, key)

            if not cache_value:
                data = func(*args, **kwargs)
                save_cache(filename, key, data, ttl)
                return data

            return cache_value

        return wrapper

    return decorate
