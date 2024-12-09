cat = False
for i in range(int(input())):
    if "кот" in input().lower():
        cat = True
        break
if cat:
    print("МЯУ")
else:
    print("НЕТ")
