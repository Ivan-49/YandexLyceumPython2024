user, nomer_posl = int(input()), int(input())

for i in range(nomer_posl - 1):
    chslo = user
    a = 0
    while chslo:
        a += chslo % 2
        chslo >>= 1
    b = a
    while b:
        user <<= 1
        b >>= 1
    user += a

print(user)
