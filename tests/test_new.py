import pytest
import json
import logging


def test_setup_logging(logger):
    assert logger is not None


def test_log_is_json(logger, caplog):
    with caplog.at_level(logging.INFO):
        message = "Test message"
        logger.log_info(message)
    assert json.dumps(caplog.text)


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


def test_redact_ssn(logger, caplog):
    with caplog.at_level(logging.INFO):
        message = "User entered SSN: 518-03-0001"
        logger.log_info(message)
    assert "[REDACT]" in caplog.text
    assert "518-03-0001" not in caplog.text


def test_redact_ccn(logger, caplog):
    with caplog.at_level(logging.INFO):
        message = "User entered credit card: 4580-1234-1234-1234"
        logger.log_info(message)
    assert "[REDACT]" in caplog.text
    assert "1234-5678-9012-3456" not in caplog.text


def test_redact_dob_slash(logger, caplog):
    with caplog.at_level(logging.INFO):
        message = "User Birth Date: 10/10/2001"
        logger.log_info(message)
    assert "[REDACT]" in caplog.text
    assert "10/10/2001" not in caplog.text


def test_redact_dob_dash(logger, caplog):
    with caplog.at_level(logging.INFO):
        message = "User Birth Date: 2001-10-10"
        logger.log_info(message)
    assert "[REDACT]" in caplog.text
    assert "2001-10-10" not in caplog.text


def test_redact_ip_address(logger, caplog):
    with caplog.at_level(logging.INFO):
        message = "Server address: 192.168.1.1"
        logger.log_info(message)
    assert "[REDACT]" in caplog.text
    assert "192.168.1.1" not in caplog.text
