# test_logger.py
from logger import logger

def test_logs():
    logger.debug("This is a DEBUG message - useful for dev tracing.")
    logger.info("This is an INFO message - good for successful events.")
    logger.warning("This is a WARNING - something unexpected happened.")
    logger.error("This is an ERROR - something went wrong but app runs.")
    logger.critical("This is a CRITICAL error - app might crash.")

if __name__ == "__main__":
    test_logs()
