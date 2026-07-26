"""
Centralized logging configuration for ETL pipeline.
"""

import logging
from pathlib import Path

LOG_PATH = Path(__file__).parent.parent.parent / "logs"
LOG_PATH.mkdir(exist_ok=True)


def _create_logger(name, file_name, level):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(LOG_PATH / file_name, encoding="utf-8")

    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger_pipeline = _create_logger("pipeline", "pipeline.log", logging.INFO)

logger_error = _create_logger("error", "error.log", logging.ERROR)
