count = 0
users = []
user = input()
while user != "!":
    user = int(user)
    count += 1
    users.append(user)
    user = input()

for i in users:
    if i < 150 or i > 190:
        users.remove(i)
        count -= 1
print(count)
print(min(users), max(users))
