nums = [int(input()) for i in range(int(input()))]

for i in range(1, len(nums) + 1):
    if len(nums) == 1:
        break
    print(nums[i - 1] + nums[i])
    if i == len(nums) - 1:
        break
