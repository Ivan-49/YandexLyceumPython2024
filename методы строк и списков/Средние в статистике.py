numbers = [float(i) for i in input().split()]
print(sum(numbers) / len(numbers), end=" ")
numbers = sorted(numbers)
if len(numbers) % 2 == 1:
    print(numbers[len(numbers) // 2])
else:
    print((numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2)
