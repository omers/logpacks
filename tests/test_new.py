import pytest
import logging
from logpack.logger import Logger


def test_setup_logging(logger):
    assert logger is not None


def test_log_info(logger, caplog):
    caplog.set_level(logging.INFO)
    logger.log_info("Test info message")
    assert "Test info message" in caplog.text


def test_log_error(logger, caplog):
    logger.log_error("Test error message")
    assert "Test error message" in caplog.text


def test_log_warning(logger, caplog):
    logger.log_warning("Test warning message")
    assert "Test warning message" in caplog.text


def test_obfuscate_message(logger, caplog):
    message = "User entered password: 123456 and credit card: 1234-5678-9012-3456"
    logger.log_info(message)
    assert (
            "User entered ********: 123456 and ***********: 1234-5678-9012-3456" 
            in caplog.text
    )
