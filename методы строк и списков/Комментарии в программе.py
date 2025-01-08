user = input()
for i in range(int(user[1:])):
    user = input()
    if str(user.find("#")) == str(0):
        print()
    elif "#" in user:
        print(user[: user.find("#")].rstrip())
    else:
        print(user.rstrip())
