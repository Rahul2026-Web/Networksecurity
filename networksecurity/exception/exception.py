import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_details: tuple):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details

    def __str__(self):
        return f"{self.error_message} | Details: {self.error_details}"

if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(str(e), sys.exc_info())










