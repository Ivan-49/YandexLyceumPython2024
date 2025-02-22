def tic_tac_toe(field: list) -> None:

    for row in field:
        if row[0] == row[1] == row[2] and row[0] != "-":
            print(row[0], "win")
            return

    for x in range(3):
        column = [row[x] for row in field]

        if column[0] == column[1] == column[2] and column[0] != "-":
            print(column[0], "win")
            return

    diag1 = [field[0][0], field[1][1], field[2][2]]
    diag2 = [field[0][2], field[1][1], field[2][0]]

    if diag1[0] == diag1[1] == diag1[2] and diag1[0] != "-":
        print(diag1[0], "win")
        return
    elif diag2[0] == diag2[1] == diag2[2] and diag2[0] != "-":
        print(diag2[0], "win")
        return
    print("draw")


data = """0 - 0
x x x
0 0 -"""

field = [line.split() for line in data.split("\n")]
tic_tac_toe(field)
