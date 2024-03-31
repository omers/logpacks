import logging
import re
import sys
from .words import sensitive_words


class Logger:
    def __init__(self, log_file="app.log"):
        self.log_file = log_file
        self.setup_logging()

    def setup_logging(self):
        log_format = '{"timestamp": "%(asctime)s", "loglevel": "%(levelname)s", "message": "%(message)s"}'
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)

    def log_warning(self, message):
        logging.warning(message)

    def obfuscate_message(self, message):
        for word in sensitive_words:
            message = re.sub(r"\b" + re.escape(word) + r"\b", "*" * len(word), message)
        return message
