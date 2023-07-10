from logging import getLogger
import sys
from inspect import stack

if sys.argv[0].find('client') == -1:
    LOGGER = getLogger('server')
else:
    LOGGER = getLogger('client')


def log(func):
    def log_saver(*args, **kwargs):
        result = func(*args, **kwargs)
        LOGGER.debug(
            f'Была вызвана функция {func.__name__} с параметрами {args}, {kwargs} '
            f'Вызов из модуля {func.__module__}. '
            f'Вызов из функции {stack()[1][3]}.', stacklevel=2)
        return result

    return log_saver
