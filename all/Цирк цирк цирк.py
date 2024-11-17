def min_steps_to_n(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        steps += 1
    return steps


n = int(input().strip())
result = min_steps_to_n(n)
print(result)
