user = int(input())
num1 = 1
num2 = 1
num3 = 0
print(1)
print(1)

while True:
    
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 > user:
        break
    print(num3)
