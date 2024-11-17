summa = 0
count = 1

a = False

user = int(input())
while True:
    summa += user
    if summa == 10:
        a = True
    if not a:
        count += 1
    user = int(input())
    if user == 0:
        break
print(count)    