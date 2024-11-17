user = input()
for index, val in enumerate(user):
    index += 1
    for i in range(index):
        print(val, end="")
