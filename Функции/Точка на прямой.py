def line(s, t):

    s = s.split("x")
    k = float(s[0])
    zn = s[1][0]
    b = float(s[1][1:])
    x, y = t.split(";")
    x, y = float(x), float(y)

    if zn == "-":
        if k * x - b == y:
            print(True)
        else:
            print(False)
    if zn == "+":
        if k * x + b == y:
            print(True)
        else:
            print(False)
