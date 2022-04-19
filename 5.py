import re

s = input("Введите полное имя файла: ")

name = re.search(r'\\([^\\]*)\.', s)[1]

print(f"Имя файла: {name}")
