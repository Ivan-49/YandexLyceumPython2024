strings = [[i for i in input().split()] for i in range(int(input()))]

restult = []
for i in strings:
    for j in i:
        restult.append(j)

for i in restult:
    if ',' in i:
        i.replace(',', '')
    if '.' in i:
        i.replace('.', '')
    if '!' in i:
        i.replace('!', '')
    if '?' in i:
        i.replace('?', '')
    if ':' in i:
        i.replace(':', '')
    if ';' in i:
        i.replace(';', '')



restult2 = {}

for i in restult:
    if i in restult2.keys():
        restult2[i] += 1
    else:
        restult2[i] = 1

for i in sorted(restult2, key=restult2.get, reverse=True):
    print(i)