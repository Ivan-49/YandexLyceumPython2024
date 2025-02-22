from sys import stdin


all = stdin

words = []
for i in all.readlines():
    words.append(i.strip())

print(min(words))
