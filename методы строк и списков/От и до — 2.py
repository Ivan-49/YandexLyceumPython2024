nums = [int(i) for i in input().split()]
range_ = [int(i) for i in input().split()]
res = 0
for i in range(range_[0], range_[1] + 1):
    res += nums[i]
print(res)
