size = int(input())

field = []

for i in range(size):
    row = []
    for j in range(size):
        count = int(input())
        row.append(count)
    field.append(row)


drops = []
count_drop = int(input())

for i in range(count_drop):
    drops.append(tuple(reversed((int(input()), int(input())))))


for drop_x, drop_y in drops:
    field[drop_x][drop_y] = max(field[drop_x][drop_y] - 4, 0)

    for offset_x in range(-1, 2):
        for offset_y in range(-1, 2):

            neighbor_x, neighbor_y = drop_x + offset_x, drop_y + offset_y

            if 0 <= neighbor_x < size and 0 <= neighbor_y < size:
                field[neighbor_x][neighbor_y] = max(
                    field[neighbor_x][neighbor_y] - 4, 0
                )


[print(*i, sep=" ") for i in field]
