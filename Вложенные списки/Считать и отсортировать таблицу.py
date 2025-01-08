count_row, count_column = int(input()), int(input())

table = [[input() for _ in range(count_column)] for _ in range(count_row)]

for index, row in enumerate(table):
    if index not in [0, count_row - 1]:
        print(*sorted(row), sep="\t")
    else:
        print(*row, sep="\t")
