user = input().upper().split()
res = []
for i in user:
    print("-".join([char for char in i]), end=" ")
