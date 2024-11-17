user = int(input())
res = 0
for i in range(1, user + 1):
    res += 1 / i ** 2
print(3.141592653589793 ** 2 / res)
