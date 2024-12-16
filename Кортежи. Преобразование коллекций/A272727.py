n = int(input())
result = [0]
for _ in range(n - 1):
    matches = sum(1 for i in range(len(result)) if result[i] == result[-i - 1])
    result.append(matches)
print(*result, sep='\n')