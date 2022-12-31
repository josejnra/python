from time import sleep

from logger import logger

if __name__ == '__main__':
    logger.info('Executando script...')
    sleep(2)
    logger.info('Execução Finalizada!')
