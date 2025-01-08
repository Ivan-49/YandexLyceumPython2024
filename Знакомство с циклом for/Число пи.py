n = int(input())
result = 0

for i in range(0, n):
    result += ((-1) ** i) / (2 * i + 1)

print(result * 4)
