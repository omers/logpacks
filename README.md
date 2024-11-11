# Logpack

Logpack is a simple logging package designed to handle application logging with additional capabilities to obfuscate sensitive information. This package provides a `Logger` class that can be used to log messages at various levels (info, warning, error) and redact sensitive information such as IP addresses, Social Security Numbers (SSNs), credit card numbers, and dates of birth.

## Features

- Log messages at different levels: info, warning, error.
- Obfuscate sensitive information in log messages.
- Configurable logging format.
- Output logs to a specified file or standard output.

## Installation

To install Logpack, clone the repository and install the dependencies:

```sh
git clone https://github.com/yourusername/logpack.git
cd logpack
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from logpacks.logger import Logger

# Initialize the logger
logger = Logger()

# Log messages
logger.log_info("This is an info message.")
logger.log_warning("This is a warning message.")
logger.log_error("This is an error message.")
```

### Obfuscating Sensitive Information

The logger automatically obfuscates sensitive information in log messages. For example:

```python
message = "User entered SSN: 518-03-0001"
logger.log_info(message)
# The logged message will be: "User entered SSN: [REDACT]"
```

### Custom Log File
By default, the logger outputs to app.log. You can specify a different log file:

```python
logger = Logger(log_file="custom.log")
```

## Running Tests

To run the tests, use pytest:

```sh
pytest
```
