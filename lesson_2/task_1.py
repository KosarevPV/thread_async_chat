import csv
import re

import chardet


def get_data():
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as f:
            content_bytes = f.read()

        detected = chardet.detect(content_bytes)

        data = content_bytes.decode(detected['encoding'])

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
        os_name_reg = re.compile(r'Название ОС:\s*\S*')
        os_name_list.append(os_name_reg.findall(data)[0].split()[2])
        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])
        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    for j in range(3):
        obj_data = list()
        obj_data.append(os_prod_list[j])
        obj_data.append(os_name_list[j])
        obj_data.append(os_code_list[j])
        obj_data.append(os_type_list[j])
        main_data.append(obj_data)

    return main_data


def write_to_csv(file):
    writer = csv.writer(file)
    for row in get_data():
        writer.writerow(row)



with open('data.csv', 'w', encoding='utf-8') as f:
    write_to_csv(f)
