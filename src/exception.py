import sys
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Gets the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # File name where the error occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Convert the error to a string
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):  # `error` should be the exception object, not its message
        super().__init__(str(error))  # Pass the string representation of the error to Exception class
        self.error_message = error_message_detail(error, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message  # Return the custom error message when str() is called on the exception

if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Divide by Zero error")
        raise CustomException(e, sys)  # Raise CustomException with the original exception and sys module
