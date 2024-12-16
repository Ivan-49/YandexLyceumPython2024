nums = [int(input()) for i in range(int(input()))]

nums_a = set()

for i in nums:
    for j in nums:
        if (i != j and nums.count(i) == 1) or (i == j and nums.count(j) > 1):
            nums_a.add(i * j)

if int(input()) in nums_a:
    print("ДА")
else:
    print("НЕТ")