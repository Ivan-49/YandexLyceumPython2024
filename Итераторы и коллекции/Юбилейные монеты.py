from sys import stdin

bash_input = [i.strip() for i in stdin.readlines() if i.strip()]
monets = []

price = 0

for i in bash_input:
    if i not in monets:
        monets.append(i)
    else:
        i = i.split()
        price += int(i[0])

print(price)
