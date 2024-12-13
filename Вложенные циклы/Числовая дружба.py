for i in range(1, 10000):
    first = 0
    second = 0
    for j in range(1, i):
        if i % j == 0:
            first += j
    for _ in range(1, first):
        if first % _ == 0:
            second += _
    if i == second and i != first and i == min(i, first):
        print(i, first)
