import json
import socket
import sys
import time
from logging import getLogger

import logs.client_log_config
from decos import log

from common.variables import ACTION, PRESENCE, TIME, USER, ACC_NAME, \
    RESPONSE, ERROR, DEF_PORT, DEF_IP_ADR
from common.utils import send_message, get_message


LOGGER_CLIENT = getLogger('client')


@log
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACC_NAME: account_name
        }
    }
    LOGGER_CLIENT.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def process_ans(message):
    LOGGER_CLIENT.debug(f'Рзабор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    try:
        server_adr = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 6535:
            LOGGER_CLIENT.critical(f'Неподходящий порт {server_port}')
            raise ValueError
    except IndexError:
        server_adr = DEF_IP_ADR
        server_port = DEF_PORT
    except ValueError:
        LOGGER_CLIENT.info('Порт должен быть в диапазоне от 1024 до 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_adr, server_port))

    message_to_server = create_presence()
    send_message(transport, message_to_server)

    try:
        answer = process_ans(get_message(transport))
        LOGGER_CLIENT.info(f'Получен ответ от сервера {answer}')
    except (ValueError, json.JSONDecodeError):
        LOGGER_CLIENT.error('Не удалось декодировать сообщение от сервера')


if __name__ == '__main__':
    main()
