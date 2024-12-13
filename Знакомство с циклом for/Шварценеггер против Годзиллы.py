def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


nums = []
for i in range(int(input())):
    prom = (int(input()), int(input()))
    nums.append(prom)

znam = 1
for i in nums:
    znam *= i[1]

res = 0
for i in nums:
    res += i[0] * znam // i[1]

fff = nod(res, znam)
print(f"{res//fff}/{znam//fff}")
