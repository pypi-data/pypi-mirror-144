[![PyPI version](https://badge.fury.io/py/plogger.svg)](https://badge.fury.io/py/plogger)
[![Build Status](https://travis-ci.org/c-pher/plogger.svg?branch=master)](https://travis-ci.org/c-pher/plogger)
[![Coverage Status](https://coveralls.io/repos/github/c-pher/plogger/badge.svg?branch=master)](https://coveralls.io/github/c-pher/plogger?branch=master)


## Plogger

Plogger - a simple high level logger wrapper to log into console/file with different level. Used built-in logger module.

## Result
```cmd
2020-01-08 02:03:47 | INFO | LOGGER_NAME log it as INFO
```

## Installation
For most users, the recommended method to install is via pip:
```cmd
pip install plogger
```

## Import

```python
from plogger import Logger
```

## Usage

- As standalone logger function:

```python
import plogger

logger = plogger.logger('NAME', level=10)

logger.info('Test message')
logger.error('Test message')
logger.warning('Test message')
logger.debug('Test message')
```

```commandline
2022-03-28 21:04:39 | INFO    | NAME | Test message
2022-03-28 21:04:39 | ERROR   | NAME | Test message
2022-03-28 21:04:39 | WARNING | NAME | Test message
2022-03-28 21:06:36 | DEBUG   | NAME | Test message
```


## Changelog

##### 1.0.4 (28.03.2022)
- added log level selection with the "level" param
- log level entry aligned

##### 1.0.3 (29.01.2022)

Fixed entries duplicating. Added handlers cleaning

##### 1.0.2 (25.01.2022)

console_output=sys.stderr by default

##### 1.0.1 (10.01.2022)

Added console_output=sys.stdout param

##### 1.0.0 (26.01.2020)

Added logger() function