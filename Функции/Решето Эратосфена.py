def eratosthenes(n):
    nums = list(range(2, n + 1))
    crossed = []
    i = 2

    while i <= n:
        for num in list(nums):
            if num != i and num % i == 0:
                nums.remove(num)
                crossed.append(num)

        next_i = None

        for num in nums:
            if num > i:
                next_i = num
                break

        if next_i is None:
            break

        i = next_i

    print(*crossed)
