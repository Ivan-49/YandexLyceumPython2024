nums = [int(input()) for i in range(int(input()))]
while nums:
    print(max(nums))
    nums.remove(max(nums))
