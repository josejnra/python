import logging
from logger import setup_logging


def main() -> None:
    """
        Execution example:
        python main.py 2>stderr.log >stdout.log
    """
    logging.info("My email: somebody@email.com")
    logging.debug('A DEBUG message')
    logging.info('An INFO message')
    logging.warning('A WARNING message')
    logging.error('An ERROR message')
    logging.critical('A CRITICAL message')


if __name__ == "__main__":
    setup_logging()
    main()
