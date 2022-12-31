from typing import Callable
from logging import LogRecord
import logging
import logging.config
import yaml


def filter_maker(level: str) -> Callable[[str], bool]:
    """filter factory function"""
    level = getattr(logging, level)

    def msg_filter(record: LogRecord):
        return record.levelno <= level

    return msg_filter


def setup_logging() -> None:
    """initialize logging"""
    with open("log_config.yaml", mode='r', encoding="utf-8") as file:
        config_dict = yaml.safe_load(file)
        logging.config.dictConfig(config_dict)
