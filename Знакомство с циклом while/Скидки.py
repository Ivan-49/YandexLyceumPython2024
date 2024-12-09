st = 0
user = float(input())
while user >= 0:
    if user > 1000:
        user = user * 0.95
    st += user
    user = float(input())
print(st)
