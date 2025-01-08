tituls = {}
for i in range(int(input())):
    user = ""
    while user != "*":
        user = input()
        if user == "*":
            break
        elif i not in tituls.keys():
            tituls[i] = []

        tituls[i].append(user)

result = []

for titul in tituls.values():
    prores = []
    for word in [word.split() for word in titul]:
        for i in word:
            prores.append(i)
    result.append("-".join((prores)))

print(", ".join(reversed(result)))
