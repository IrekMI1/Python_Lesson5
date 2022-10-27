# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

some_text = input('Ввдите текст: ').split()
new_text = []
for word in some_text:
    if 'абв' not in word:
        new_text.append(word)
print(new_text)