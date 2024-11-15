num1 = float(input())
num2 = float(input())
str_ = input()

if str_ in ['+', '-', '*', '/']:
    if str_ == '+':
        print(num1 + num2)
    elif str_ == '-':
        print(num1 - num2)
    elif str_ == '*':
        print(num1 * num2)
    else:
        if num2 == 0.0:
            print(888888)
        else:
            print(num1 / num2)
else:
    print(888888)