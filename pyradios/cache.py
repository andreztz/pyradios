import pickle
import time
from functools import wraps

from pyradios.log import logger
from pyradios.utils import setup_cache_file


def write_file(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def read_file(filename):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return data
    except IOError as exc:
        logger.exception("File not Found: {}".format(filename))
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


def save_cache(filename, key, value, expire):
    data = read_file(filename)
    expiry = time.time() + int(expire)
    data[key] = (expiry, value)
    write_file(filename, data)


def cache(filename, expire, **kwargs):

    filename = setup_cache_file(filename, **kwargs)

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not expire:
                return func(*args, **kwargs)

            key = func.__name__
            cache_value = read_cache(filename, key)

            if not cache_value:
                data = func(*args, **kwargs)
                save_cache(filename, key, data, expire)
                return data

            return cache_value

        return wrapper

    return decorate
