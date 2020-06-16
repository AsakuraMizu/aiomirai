import logging
import sys

default_handler = logging.StreamHandler(sys.stdout)
default_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] [Mirai %(name)s] %(levelname)s: %(message)s'
))


def get_logger(name: str, level: int) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(default_handler)
    logger.setLevel(level)
    return logger


Api = get_logger('Api', logging.INFO)
Receiver = get_logger('Receiver', logging.INFO)
