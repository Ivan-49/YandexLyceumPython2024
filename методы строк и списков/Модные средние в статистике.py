numbers = [float(i) for i in input().split()]

print(int(sorted(numbers)[len(numbers) // 2]), end=" ")

result = {}

for i in numbers:
    if i not in result.keys():
        result[i] = numbers.count(i)

print(int(max(result, key=result.get)))
