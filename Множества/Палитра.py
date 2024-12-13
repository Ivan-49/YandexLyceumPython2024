count_colors = {}
repeaters = set()

for i in range(int(input())):
    for j in range(int(input())):
        tmp = input()
        count_colors[tmp] = count_colors.get(tmp, 0) + 1
        if count_colors[tmp] > 1:
            repeaters.add(tmp)

print(len(repeaters), sum(map(count_colors.get, repeaters)))
