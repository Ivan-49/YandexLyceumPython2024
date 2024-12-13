recomendations = [input().lstrip() for i in range(int(input()))]

for i in recomendations:
    if not ("Не " in i[:3] or "не " in i[:3]):
        print(i)
    else:
        print(i[3:])
