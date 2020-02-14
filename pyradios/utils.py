from pathlib import Path

from pyradios.config import app_dirs


class Error(Exception):
    """Base class for all excpetions raised by this module."""


class IllegalArgumentError(Error):
    """Raised for illegal argument"""
    pass


def create_app_dirs(filename, path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p / filename


def setup_log_file(filename, **kwargs):
    return create_app_dirs(filename, app_dirs.user_log_dir)


def setup_cache_file(filename, **kwargs):
    return create_app_dirs(filename, app_dirs.user_cache_dir)


def bool_to_string(b):
    """Convert a boolean type to string.

    Args:
        b (bool): A Boolean.

    Raises:
        ValueError: [description]

    Returns:
        str: String representation of a bool type.
    """
    s = str(b).lower()
    if s in ["true", "false"]:
        return s
    raise TypeError("Value must be True or False.")


def snake_to_camel(s):
    first, *others = s.split('_')
    return "".join([first.lower(), *map(str.title, others)])


def input_validate(params, valid):
    for key, value in params.items():
        try:
            type_ = valid[key]
        except KeyError as exc:
            raise IllegalArgumentError(
                "There is no paramter named '{}'".format(exc.args[0])
            )
        else:
            if not isinstance(value, type_):
                raise TypeError(
                    "Argument {!r} must be {}, not {}".format(
                        key, type_.__name__, type(value).__name__,
                    )
                )
