size = int(input())
table = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    table.append(row)


for row in table[1:]:
    user_input = [int(i) for i in input().split()]
    for col in range(len(user_input)):
        row[col] = user_input[col]

invert_table = []

for i in range(size):
    row = []
    for j in range(size):
        row.append(table[j][i])
    invert_table.append(row)

for i in range(size):
    for j in range(size):
        if i == j:
            table[i][j] = 0
        if i > j:
            table[j][i] = invert_table[j][i]


for i in table:
    print(*i)
