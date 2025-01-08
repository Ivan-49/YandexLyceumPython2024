user = input().lower()

res = set()

for i in user:
    res.add((i, user.count(i)))

print(max(res, key=lambda x: x[1])[1])
