import sys
import logging
import src.logger as logging

def error_message_detail(error, error_detail: sys):
    # (type(e), e, e.__traceback__)
    _,_,exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python file name [{}] line number [{}] error message [{}]".format(
        file_name, exec_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def str(self):
        return self.error_message


""" if __name__ == "__main__":
    try: 
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys) """