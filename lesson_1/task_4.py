"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

data = ("разработка", "администрировани", "protocol", "standard")

for item in data:
    print(f'{item} - {type(item)}')
    item = item.encode('utf-8')
    print(f'{item} - {type(item)}')
    item = item.decode('utf-8')
    print(f'{item} - {type(item)}\n')
