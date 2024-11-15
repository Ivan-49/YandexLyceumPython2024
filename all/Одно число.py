
number = float(input())

if abs(number) < 0.000001:
    print(1000000)
else:
    inverse = 1 / number 
    print(inverse)
