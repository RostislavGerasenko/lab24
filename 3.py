import re

s = input("Введите строку: ")
number = 1

while number:
   s, number = re.subn(r'(^| )([А-Я])([А-Я]*)(\2)', r'\1\2\3.', s)

print(f"Новая строка: {s}")
