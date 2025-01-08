len_ = int(input())

for i in range(int(input())):
    user = input()
    if len_ < len(user):
        print(user[: len_ - 3] + "...")
    else:
        print(user)
