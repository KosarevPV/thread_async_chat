"""Константы"""

import logging


# Порт и IP адрес по умолчанию
DEFAULT_PORT = 7777
DEFAULT_IP_ADDRESS = '127.0.0.1'

# Максимальная очередь подключений
MAX_CONNECTIONS = 5

# Максимальная длина сообщения
MAX_PACK_LEN = 1024

# Кодировка
ENCODING = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'


# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'

LOGGING_LEVEL = logging.DEBUG

# Словари - ответы:
# 200
RESPONSE_200 = {RESPONSE: 200}
# 400
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
