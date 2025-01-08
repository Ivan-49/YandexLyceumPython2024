alphavit_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alphavit_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

user = set(input())
result = []
for i in user:
    if i in alphavit_en:
        print((i, alphavit_en.index(i) + 1))
    elif i in alphavit_rus:
        print((i, alphavit_rus.index(i) + 1))
