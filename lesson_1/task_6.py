import chardet


with open('test_file.txt', 'w') as f:
    f.write('сетевое программирование\nсокет\nдекоратор')

with open('test_file.txt', 'rb') as f:
    content_bytes = f.read()

print(content_bytes)
detected = chardet.detect(content_bytes)
print(detected)
content_text = content_bytes.decode(detected['encoding'])

with open('test_file_utf_8.txt', 'w', encoding='utf-8') as f:
    f.write(content_text)

with open('test_file_utf_8.txt', 'r', encoding='utf-8') as f:
    print(f.read())

