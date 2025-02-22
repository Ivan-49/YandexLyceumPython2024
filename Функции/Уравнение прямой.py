def equation(a, b):
    x1, y1, x2, y2 = (*a.split(";"), *b.split(";"))
    x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])

    if y1 == y2:
        print(y1)
        return
    if x1 == x2:
        print(x1)
        return

    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1

    print(k, b)
