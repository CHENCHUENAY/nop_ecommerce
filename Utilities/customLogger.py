import logging
import time

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename = './Logs/test_001.log',
            #'''level = logging.INFO,'''
            format = '%(asctime)s: %(levelname)s: %(message)s:',
            datefmt = '%D:%M:%Y %H:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


  