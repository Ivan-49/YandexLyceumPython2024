SUITS = ["пик", "треф", "бубен", "червей"]
names_cards = ["валет", "дама", "король", "туз"]
user = input()
del SUITS[SUITS.index(user)]

for i in range(2, 11):
    for j in SUITS:
        print(f"{i} {j}")
for i in names_cards:
    for j in SUITS:
        print(f"{i} {j}")
