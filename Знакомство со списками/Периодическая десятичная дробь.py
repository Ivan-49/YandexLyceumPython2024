def calculate_fractional_part(number):
    remainders = []
    digits = []
    remainder = 1

    while remainder not in remainders:
        remainders.append(remainder)
        digits.append(remainder * 10 // number)
        remainder = 10 * remainder % number
    
    start_index = remainders.index(remainder)
    return "".join(map(str, digits[start_index:]))


print(calculate_fractional_part(int(input())))