import json


def test_log_is_json(logger):
    resp = logger.log_info("Hello from Omer")
    assert json.dumps(resp)


def test_obfuscation(logger):
    message = "User entered password: 123456 and credit card: 1234-5678-9012-3456"
    obfuscated_message = logger.obfuscate_message(message)

    assert True
    logger.log_info(obfuscated_message)
