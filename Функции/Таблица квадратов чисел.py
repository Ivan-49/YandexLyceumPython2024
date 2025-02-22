def squared(a, b, k):
    rpw = ""
    for i in range(a, b + 1):
        if i**2 % k != 0:
            rpw += f"{i ** 2:<5}"
        if str(a - 1)[-1] == str(i)[-1]:
            print(rpw)
            rpw = ""
        if i == b and rpw != "":
            print(rpw)


squared(11, 99, 10)
print()
squared(4, 33, 9)
print()
squared(22, 64, 5)
