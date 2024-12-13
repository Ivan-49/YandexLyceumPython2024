accuracy = int(input())
pi = 4.0
sign = -1
denominator = 2
precision = 0.1**accuracy

while True:
    term = 4 / (denominator * (denominator + 1) * (denominator + 2)) * sign
    pi += term
    sign *= -1
    denominator += 2
    if abs(term) < precision:
        break


print(pi)
