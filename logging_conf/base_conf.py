import logging
from logging.handlers import RotatingFileHandler


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler('logs.log',
                                       maxBytes=50000000,
                                       backupCount=5)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    return logger
