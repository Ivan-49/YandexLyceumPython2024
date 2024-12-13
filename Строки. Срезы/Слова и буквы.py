user = input()
res = {}

while user != "стоп":
    res[user] = len(user)
    user = input()

min_ = min(res, key=len)
max_ = max(res, key=len)

res = []
for i in min_:
    if i in max_:
        res.append(i)
if len(res) == len(min_):
    print("ДА")
else:
    print("НЕТ")
