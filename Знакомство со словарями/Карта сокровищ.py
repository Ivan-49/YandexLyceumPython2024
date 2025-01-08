count_point = int(input())

cords = []
result = []

for i in range(count_point):
    x, y = input().split()

    if len(x) == 1:
        x = "0" + x
    if len(y) == 1:
        y = "0" + y

    if len(x) > 1:
        x = x[:-1]
    if len(y) > 1:
        y = y[:-1]
    cords.append((x, y))

for i in cords:
    result.append(cords.count(i))

print(max(result))
