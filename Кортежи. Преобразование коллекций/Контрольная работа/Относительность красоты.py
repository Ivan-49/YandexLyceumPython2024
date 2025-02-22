res = set()

for i in [input() for _ in range(int(input()))]:
    if len(i) > 1:
        res.add(int(f"{i[0] + i[1] + i[- 1]}"))
    else:
        res.add(int(f"{i + i}"))

res = sorted(res)

for i in sorted(res):
    print(i, end=" ")
