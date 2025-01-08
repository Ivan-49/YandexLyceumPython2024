number = [bin(int(i))[2:] for i in input().split()]

result = []

for i in number:
    specifications = {
        "digits": len(str(i)),
        "units": i.count("1"),
        "zeros": i.count("0"),
    }
    result.append(specifications)
print(result)
