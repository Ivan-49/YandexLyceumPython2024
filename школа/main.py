user = input()
users = []

while user != "СТОП":
    users.append(user)
    user = input()

max_len = len(max(users, key=len))
count = 0

for user in users:
    if max_len == len(user):
        count += 1

print(count)
