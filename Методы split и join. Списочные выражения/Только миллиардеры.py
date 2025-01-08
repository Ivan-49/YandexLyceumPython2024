magains = input().split(";")
for i in magains:
    res = []
    [res.append(int(a)) for a in i.split(",") if int(a) >= 1_000_000_000]
    print(*res, sep=",")
