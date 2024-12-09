x = y = steps = 0
xt = int(input())
yt = int(input())
while True:
    if x == xt and y == yt:
        print(steps)
        break

    head = input()
    if head == "запад" or head == "восток":
        x = {"восток": lambda n: x + n, "запад": lambda n: x - n}[head](int(input()))
    if head == "север" or head == "юг":
        y = {"север": lambda n: y + n, "юг": lambda n: y - n}[head](int(input()))
    steps = steps + 1
