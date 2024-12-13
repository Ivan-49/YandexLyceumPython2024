word = input()
index = int(input())
letter = input()
love_letter = letter if len(letter) == 1 else None

if (not (love_letter)) or index > len(word) or index < 1:
    print('ОШИБКА')
    exit()

if word[index - 1] == love_letter:
    print('ДА')
else:
    print('НЕТ')