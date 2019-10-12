from pathlib import Path

from pyradios.config import app_dirs


def create_app_dirs(filename, path):
    p = Path(path)
    if not p.exists():
        p.mkdir(parents=True)
    return p / filename


def setup_log_file(filename, **kwargs):
    return create_app_dirs(filename, app_dirs.user_log_dir)


def setup_cache_file(filename, **kwargs):
    return create_app_dirs(filename, app_dirs.user_cache_dir)
