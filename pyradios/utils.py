from pathlib import Path

from pyradios.config import app_dirs


def create_app_dirs(filename, path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p / filename


def setup_log_file(filename, **kwargs):
    return create_app_dirs(filename, app_dirs.user_log_dir)


def setup_cache_file(filename, **kwargs):
    return create_app_dirs(filename, app_dirs.user_cache_dir)


def bool2string(b):
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
