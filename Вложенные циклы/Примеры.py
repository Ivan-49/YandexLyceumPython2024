first = int(input())
second = int(input())
step = int(input())

for i in range(first, second + 1, step):
    res = ""
    for j in range(first, second + 1, step):
        res += f'{i} + {j} = {i + j}\t'       
    print(res)