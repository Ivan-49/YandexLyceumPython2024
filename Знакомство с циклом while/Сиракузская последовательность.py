num = int(input())
count = 0
while num != 1:
    if num % 2 != 0:
        num = num * 3 + 1
    else:
        num /= 2
    count += 1
print(count)
