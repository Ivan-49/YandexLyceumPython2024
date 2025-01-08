user_way = input()
way = user_way[1::].replace("V", "!V!").split("!")
position = 0
k = 0
if len(user_way) == 1:
    print(user_way[0])
    exit()
for i in way:
    if i:
        if i == "V":
            print(user_way[0])
            break
        else:
            break
for i in way:

    if not i:
        continue
    elif i[0] == "<":
        position -= len(i)
        print(position * " " + user_way[0] + i.replace("<", user_way[0]))
        k = 0
    elif i[0] == ">":
        print(position * " " + user_way[0] + i.replace(">", user_way[0]))
        position += len(i)
        k = 0
    elif i[0] == "V":
        if k:
            print(position * " " + user_way[0])
        k = 1
if k:
    print(position * " " + user_way[0])
