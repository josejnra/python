import logging.config

import yaml


def setup_logging() -> None:
    """initialize logging"""
    with open("log_config.yaml", encoding="utf-8") as file:
        config_dict = yaml.safe_load(file)
        logging.config.dictConfig(config_dict)
