import logging
import sys

default_handler = logging.StreamHandler(sys.stdout)
default_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] [Mirai %(name)s] %(levelname)s: %(message)s'
))

def Logger(name: str, level: int) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(default_handler)
    logger.setLevel(level)
    return logger

Api = Logger('Api', logging.INFO)
Receiver = Logger('Receiver', logging.INFO)
