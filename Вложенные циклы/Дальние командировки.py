user = int(input())
count = 0

for i in range(1, user + 1):
    user -= len(str(i))
    count += 1
    if user <= 0:
        print(count)
        break
