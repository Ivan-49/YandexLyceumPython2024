user = {"x": 0, "y": 0, "direction": "север"}
directions = ["север", "восток", "юг", "запад"]
qasdasdsd = {"север": ["y", 1], "восток": ["x", 1], "юг": ["y", -1], "запад": ["x", -1]}

x, y = int(input()), int(input())

min = 0
direction = 0
user1 = ""
while not (user["x"] == x and user["y"] == y):
    user1 = input()
    if user1 == "вперёд":
        user[qasdasdsd[directions[direction]][0]] += (
            int(input()) * qasdasdsd[directions[direction]][1]
        )
        min += 1
    elif user1 == "налево":
        direction += -1
        min += 1
    elif user1 == "направо":
        direction += 1
        min += 1
    elif user1 == "разворот":
        direction -= 2
        min += 1

    if direction == -5:
        direction = 3

print(min)
print(directions[direction])
