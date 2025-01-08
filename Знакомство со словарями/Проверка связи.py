string = input().split()

dictory = {}

result = []
for i in range(len(string)):
    if string[i] not in dictory.keys():
        dictory[string[i]] = 1
    else:
        dictory[string[i]] += 1
    result.append(dictory[string[i]])

print(*result)
