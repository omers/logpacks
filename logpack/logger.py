import logging
import re
import sys

class Logger:
    def __init__(self, log_file="app.log"):
        self.log_file = log_file
        self.setup_logging()

    def _obfuscate_message(self, message):
        sensitive_patterns = [
            (r"\b(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})\b", '[REDACT]'),
            (r"\b\d{4}-\d{4}-\d{4}-\d{4}\b", '[REDACT]'),
            (r"\b\d{2}/\d{2}/\d{4}\b", "[REDACT]"),
            (r"\b\d{4}-\d{2}-\d{2}\b", "[REDACT]"),
            (r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "[REDACT]")
        ]

        for pattern, replacement in sensitive_patterns:
            message = re.sub(pattern, replacement, message)

        return message

    def setup_logging(self):
        log_format = '{"timestamp": "%(asctime)s", "loglevel": "%(levelname)s", "message": "%(message)s"}'
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

    def log_info(self, message):
        message = self._obfuscate_message(message)
        logging.info(message)

    def log_error(self, message):
        message = self._obfuscate_message(message)
        logging.error(message)

    def log_warning(self, message):
        message = self._obfuscate_message(message)
        logging.warning(message)
