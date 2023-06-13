"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

data = ("class", "function", "method")

for item in data:
    print(f'{item} - {type(item)}, len - {len(item)}')
    item = bytes(item, encoding='utf-8')
    print(f'{item} - {type(item)}, len - {len(item)}\n')
