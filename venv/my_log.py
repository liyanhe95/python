import logging
import logging.handlers
from common import contants
from common.config import ReadConfig

config = ReadConfig()
def get_logger(file_name):
    logger = logging.getLogger()


