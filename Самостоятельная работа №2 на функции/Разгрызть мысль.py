from sys import stdin


input_data = stdin.readlines()

count = 0

strings = []

for line in input_data:
    count += 1
    strings.append(line.strip().lower())

while count % 3 != 0:
    count -= 1
    del strings[-1]

for i in range(0, count, 3):
    string = strings[i] + " " + strings[i + 1] + " " + strings[i + 2]
    max_len = 0
    for i in string.split():
        if len(i) > max_len:
            max_len = len(i)
    prores = []
    for i in string.split():
        if len(i) == max_len and i not in prores:
            prores.append(i)

    print(": ".join(sorted(prores)))
