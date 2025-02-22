import math


def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (1 - phi) ** n) / math.sqrt(5))


def golden_ratio(n):
    print(fibonacci_binet(n + 1) / fibonacci_binet(n))
