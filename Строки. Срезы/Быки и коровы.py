first, second = input(), input()

res1 = []
res2 = []

for i in range(len(first)):
    if first[i] == second[i]:
        res1.append(first[i])

for i in range(len(first)):
    if first[i] in second and first[i] != second[i]:
        res2.append(first[i])

print(len(res1), len(res2))