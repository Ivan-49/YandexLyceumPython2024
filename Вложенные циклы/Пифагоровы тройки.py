limit = int(input())

for m in range(2, int(limit**0.5) + 1):
    for n in range(1, m):
        if (m - n) % 2 == 1 and (gcd := lambda a, b: a if b == 0 else gcd(b, a % b))(
            m, n
        ) == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            if c <= limit:
                print(a, b, c)
            else:
                break
