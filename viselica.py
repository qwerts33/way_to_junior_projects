words = ["питон", "программа", "клавиатура", "функция", "переменная",
         "список", "условие", "цикл", "строка", "словарь"]

max_count = 6

from random import choice

answer = choice(words)
secret = ['_'] * len(answer)
used = set()
count = 0
while True:
    if count > max_count:
        print('Проигрыш')
        break
    print(*secret)
    print(6-count)
    print(f'Использованные буквы:{(list(used))}')
    print("Введите букву")
    letter = input()
    if len(letter) != 1:
        print("Введите одну букву")
        continue
    if letter in used:
        print("Буква уже использовалась")
        continue
    used.add(letter)
    if letter in answer:
        for i,char in enumerate(answer):
            if char == letter:
                secret[i] = letter
    else:
        count+=1
    if ''.join(secret) == answer:
        print("Победа")
        break

