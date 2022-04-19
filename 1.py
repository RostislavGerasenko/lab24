import re

s = input("Введите строку: ")
count = re.findall("^\S| \S", s)

print(f"Число слов в строке: {len(count)}")
