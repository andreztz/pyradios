import logging

from pyradios.utils import setup_log_file

LOG_FILENAME = "pyradios.log"

logger = logging.getLogger(__name__)

formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
)
file_handler = logging.FileHandler(setup_log_file(LOG_FILENAME))
file_handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
