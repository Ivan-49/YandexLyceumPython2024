from itertools import combinations


suits = ["бубен", "треф", "червей", "пик"]
values = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "валет",
    "дама",
    "король",
    "туз",
]
deck = [f"{value} {suit}" for suit in suits for value in values]
all_combinations = list(combinations(deck, 3))
valid_combinations = []

for combination in all_combinations:
    combination = sorted(combination)
    cherv = False
    bol_10 = False
    for card in combination:
        if "червей" in card:
            cherv = True
        if card[0] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            bol_10 = True
    if cherv and bol_10:
        valid_combinations.append(combination)

valid_combinations = sorted(valid_combinations)

for combination in valid_combinations:
    print(*combination, sep=", ")
