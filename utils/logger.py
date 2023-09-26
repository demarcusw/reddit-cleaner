import logging


class MyLogger:
    def __init__(self, logger_name: str, log_location: str = None):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # create a file handler
        if log_location:
            handler = logging.FileHandler(log_location)
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        # create a stream handler for stdout as well
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        stream_handler.setFormatter(stream_formatter)
        self.logger.addHandler(stream_handler)

    def log(self, message, level=logging.DEBUG):
        # custom switch. based on logging level,
        # call corresponding logger function.
        # we store in dictionary for O(1) lookup
        log = {
            logging.DEBUG: self.logger.debug,
            logging.INFO: self.logger.info,
            logging.WARNING: self.logger.warning,
            logging.ERROR: self.logger.error,
            logging.CRITICAL: self.logger.critical,
        }

        # call our specific logger level function
        log[level](message)
