s = input("Введите строку: ")
words = [len(word) for word in s.split(' ') if word]

print(f"Длинна самого короткого слова: {min(words)}")
