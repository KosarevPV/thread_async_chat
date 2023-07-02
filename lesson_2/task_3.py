import yaml

data = {
    'key_1': [1, 2, 3, 4, 5],
    'key_2': 33,
    'key_3': {'1': '1\u20ac', '2': '2\u20ac', '3': '3\u20ac', '4': '4\u20ac'},
}

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


with open('file.yaml', 'r', encoding='utf-8') as f:
    data_2 = yaml.load(f, Loader=yaml.FullLoader)

print(data_2 == data)