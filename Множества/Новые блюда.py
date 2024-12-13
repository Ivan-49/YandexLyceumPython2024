dishes_true = [input() for _ in range(int(input()))]

dishes_past = {}

for i in range(int(input())):
    count = int(input())
    today = []
    for _ in range(count):
        dish = input()
        today.append(dish)
    dishes_past[i] = today

for i in dishes_past:
    for dish in dishes_past[i]:
        if dish in dishes_true:
            dishes_true.remove(dish)
print(*dishes_true, sep="\n")
