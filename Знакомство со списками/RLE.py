user = input()

count = 0
old = user[0]

for num in user:
    if num == old:
        count += 1
    else:
        print(count, old)
        count = 1
        old = num
print(count, num)
