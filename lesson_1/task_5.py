"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess


import chardet


resource_data = ('yandex.ru', 'youtube.com')

for item in resource_data:
    ARGS = ['ping', item]
    RES_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in RES_PING.stdout:
        print(line.decode(encoding=chardet.detect(line)['encoding']))