s = input("Введите строку: ")

count = sum(s.count(char) for char in "АЕЁЁИОУЫЭЮЯаеёиоуыэюя")

print(f"Число гласных букв в строке: {count}")
