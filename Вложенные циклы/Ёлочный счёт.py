n = int(input())

count = 1
for i in range(1, n + 1):
    for j in range(count, count + i):
        print(j, end=" ")
        if j == n:
            break
    count += i
    print()
    if j == n:
        break
