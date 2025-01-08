permissions = {}

for _ in range(int(input())):
    user = input()
    permissions[user] = permissions.get(user, "")

for _ in range(int(input())):
    path = ""
    for part in input().split("/"):
        if part:
            path += "/" + part
            if path in permissions:
                print("YES")
                break
    else:
        print("NO")
