def larger_root(p, q):
    roots = get_roots(p, q)
    if len(roots) > 1:
        return max(roots)
    else:
        return roots[0]


def smaller_root(p, q):
    roots = get_roots(p, q)
    if len(roots) > 1:
        return min(roots)
    else:
        return roots[0]


def get_roots(p, q):

    D = discriminant(1, p, q)
    sqrt_D = D**0.5

    x1 = (-p + sqrt_D) / 2
    x2 = (-p - sqrt_D) / 2
    if x1 == x2:
        return [x1]
    if D < 0:
        return []
    return x1, x2


def discriminant(a: float = 1, b: float = 1, c: float = 1):
    return (b**2) - (4 * a * c)


def main():
    p, q = float(input()), float(input())

    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
