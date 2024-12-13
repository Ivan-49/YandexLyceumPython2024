count = int(input())

users = []
srednee = 0
for i in range(count):
    user = int(input())
    users.append(user)
    if srednee == 0 or srednee == user:
        print(0)
    elif srednee > user:
        print("<")
    elif srednee < user:
        print(">")
    srednee = sum(users) / len(users)
