res = [1, 1, 1]

for i in range(75):
    res.append(res[- 1] + res[- 2] + res[- 3])

print(*res[:int(input())])