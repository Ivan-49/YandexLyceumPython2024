words = [input() for i in range(int(input()))]
result = []

while words:
    a = min(words, key=len)
    result.append(a)
    words.remove(a)

for _ in range(15):
    for i in range(len(result) - 1):
        if len(result[i]) == len(result[i + 1]):
            result[i], result[i + 1] = min(result[i], result[i + 1]), max(result[i], result[i + 1])

print(*result, sep="\n")