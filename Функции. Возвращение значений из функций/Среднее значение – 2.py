def number_in_english(n):
    a = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    b = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
    c = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if 0 <= n <= 9:
        return a[n]
    elif 10 <= n <= 19:
        return b[n]
    elif 20 <= n <= 99:
        x = (n // 10) * 10
        y = n % 10
        if y == 0:
            return c[x]
        else:
            return c[x] + " " + a[y]
    elif 100 <= n <= 999:
        p = n // 100
        q = n % 100
        if q == 0:
            return a[p] + " hundred"
        else:
            if q <= 9:
                return a[p] + " hundred and " + a[q]
            elif 10 <= q <= 19:
                return a[p] + " hundred and " + b[q]
            else:
                z = (q // 10) * 10
                w = q % 10
                if w == 0:
                    return a[p] + " hundred and " + c[z]
                else:
                    return a[p] + " hundred and " + c[z] + " " + a[w]
    else:
        return "Out"
