number = input()
reversed_number = ""

for digit in number:
    reversed_number = digit + reversed_number

print(int(reversed_number))
