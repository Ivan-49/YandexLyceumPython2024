res = []

user = input()


while user:
    user = int(user)
    prores = []
    while user != -1:
        prores.append(user)
        user = int(input())
    res.append(set(prores))
    user = input()
total_res = []
[total_res.extend(i) for i in res]
del res

print(*[i for i in total_res if total_res.count(i) == 1])
