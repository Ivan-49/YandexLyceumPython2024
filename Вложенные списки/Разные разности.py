differences = set()

nums = [int(input()) for i in range(int(input()))]

for i in nums:
    for j in nums:
        differences.add(i - j)

print(*sorted([*differences]), sep="\n")
