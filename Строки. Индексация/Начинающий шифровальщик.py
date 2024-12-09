user = input()
for index, val in enumerate(user):
    print(ord(val), end="")
    if index < len(user) - 1:
        print(", ", end="")
