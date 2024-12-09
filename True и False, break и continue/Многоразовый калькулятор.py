from math import factorial

while True:
    num1 = int(input())
    op = input()
    try:
        result = {
            "+": lambda x: x + int(input()),
            "-": lambda x: x - int(input()),
            "*": lambda x: x * int(input()),
            "/": lambda x: x // int(input()),
            "%": lambda x: x % int(input()),
            "!": lambda x: factorial(x),
            "x": lambda x: x,
        }[op](num1)
        print(result)
        if op == "x":
            break
    except Exception:
        continue
