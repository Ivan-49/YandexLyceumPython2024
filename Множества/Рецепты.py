refrigerator = [input() for _ in range(int(input()))]
dishes = {}
for i in range(int(input())):
    name = input()
    ingredients = [input() for _ in range(int(input()))]
    dishes[name] = ingredients

for i in dishes:
    count = len(dishes[i])
    for _ in dishes[i]:
        if _ in refrigerator:
            count -= 1
    if count == 0:
        print(i)
