import re

s = input("Введите полное имя файла: ")

name = re.search(r'\\([^\\]*)\\[^\\]*\.', s)[1] if s.count('\\') > 1 else re.search(r'^([^\\]*)\\[^\\]*\.', s)[1] if s.count('\\') == 1 else '\\'

print(f"Какталог, содержащий файл: {name}")

