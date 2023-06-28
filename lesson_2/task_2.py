import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['orders'].append({'item': item, 'quantity': quantity, 'price': price,
                          'buyer': buyer, 'date': date})
    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


write_order_to_json(1, 2, 3, 4, 5)
write_order_to_json(1, 2, 3, 4, 5)
write_order_to_json(1, 2, 3, 4, 5)