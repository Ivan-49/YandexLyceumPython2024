a = False
for i in range(int(input())):
    i = input()
    if "Кот" in i or "кот" in i:
        a = True
    if "Пёс" in i or "пёс" in i:
        a = False
if a:
    print("МЯУ")
else:
    print("НЕТ")
