import sys
from networksecurity.logging import logger

class NetworkSecuriyException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"error occured in python script name {self.filename} line number {self.line_no} error message {self.error_message}"
    
if __name__ == "__main__":
    try:
        logger.logging.info("enter the try block")
        a = 1/0
        print("this wii not be printed", a)

    except Exception as e :
        raise NetworkSecuriyException(e,sys)
        