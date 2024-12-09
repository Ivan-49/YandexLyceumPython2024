user = int(input())
d = []
for i in range(1, user + 1):
    if user % i == 0:
        d.append(i)
print(*d)
if len(d) == 2:
    print("ПРОСТОЕ")
else:
    print("НЕТ")
