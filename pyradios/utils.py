from functools import wraps


types = {
    "search": {
        "name": str,
        "name_exact": bool,
        "codec": str,
        "codec_exact": bool,
        "country": str,
        "country_exact": bool,
        "countrycode": str,
        "state": str,
        "state_exact": bool,
        "language": str,
        "language_exact": bool,
        "tag": str,
        "tag_exact": bool,
        "tag_list": str,
        "bitrate_min": int,
        "bitrate_max": int,
        "order": str,
        "reverse": bool,
        "offset": int,
        "limit": int,
        "hidebroken": bool,  # Not documented in the "Advanced Station Search"
    },
    "countries": {"code": str},
    "countrycodes": {"code": str},
    "codecs": {"codec": str},
    "states": {"country": str, "state": str},
    "languages": {"language": str},
    "tags": {"tag": str},
}


class Error(Exception):
    """Base class for all excpetions raised by this module."""

    pass


class IllegalArgumentError(Error):
    """Raised for illegal argument"""

    pass


def bool_to_string(b):
    """Convert a boolean type to string.

    Args:
        b (bool): A Boolean.

    Raises:
        TypeError

    Returns:
        str: String representation of a bool type.
    """
    s = str(b).lower()
    if s in ["true", "false"]:
        return s
    raise TypeError("Value must be True or False.")


def snake_to_camel(s):
    first, *others = s.split("_")
    return "".join([first.lower(), *map(str.title, others)])


def radio_browser_adapter(**kwargs):
    params = {}

    for key, value in kwargs.items():
        new_key = snake_to_camel(key)
        if isinstance(kwargs[key], bool):
            value = bool_to_string(value)
        params[new_key] = value
    return params


def validate_input(types, input_data):
    for key, value in input_data.items():
        try:
            type_ = types[key]
        except KeyError as exc:
            raise IllegalArgumentError(
                "There is no paramter named '{}'".format(exc.args[0])
            )
        else:
            if not isinstance(value, type_):
                raise TypeError(
                    "Argument {!r} must be {}, not {}".format(
                        key,
                        type_.__name__,
                        type(value).__name__,
                    )
                )


def type_check(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        validate_input(types[func.__name__], kwargs)
        kwargs = radio_browser_adapter(**kwargs)
        return func(self, *args, **kwargs)

    return wrapper
