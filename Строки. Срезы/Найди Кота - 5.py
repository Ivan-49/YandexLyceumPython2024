strings = [input() for i in range(int(input()))]

for i in strings:
    if "кот" in i or "Кот" in i:
        print(strings.index(i) + 1, i.lower().index("кот") + 1)
