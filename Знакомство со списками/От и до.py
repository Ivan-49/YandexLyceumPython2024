list_ = [input() for _ in range(int(input()))]

min_, max_ = int(input()), int(input())
count = 0
res = 0
for i in list_:
    count += 1
    if (min_ <= count) and (count <= max_):
        res += int(i)

print(res)
