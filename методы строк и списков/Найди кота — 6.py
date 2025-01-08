srings = [input() for i in range(int(input()))]
[print(srings.index(i) + 1, i.index("кот") + 1) for i in srings if "кот" in i]
