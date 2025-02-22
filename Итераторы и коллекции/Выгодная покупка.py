from sys import stdin


all = stdin

name_of_book = all.readline().strip().split("\t")
shops = []
for i in all.readlines():
    shops.append(i.strip().split("\t"))

shops2 = []
for shop in shops:
    shops2.append([shop[0], sum([int(i) for i in shop[1:]])])

shops2 = min(shops2, key=lambda x: x[1])


for i in shops:
    if i[0] == shops2[0]:
        print(i[0])
        for index, val in enumerate(name_of_book):
            print(f"{val}\t{[j[index + 1] for j in shops if j[0] == i[0]][0]}")
