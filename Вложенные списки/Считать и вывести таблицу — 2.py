count_rows, count_columns = int(input()), int(input())

table = [[input() for i in range(count_columns)] for _ in range(count_rows)]

for row in table:
    print(*row, sep="\t")
print()
result = []
for i in range(count_columns):
    a = []
    for row in table:
        a.append(row[i])
    result.append(a)

for i in result:
    print(*i, sep="\t")
