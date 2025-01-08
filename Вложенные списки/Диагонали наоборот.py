def sum_diagonals(matrix: list[list[int]]) -> int:
    total_sum = 0

    for i in range(len(matrix)):
        num = matrix[i][i]
        total_sum += num

    for i in range(len(matrix)):
        num = matrix[i][-i - 1]
        total_sum += num

    return total_sum


def revers_diagonal(matrix: list[list[int]]) -> list[list[int]]:

    for i in range(len(matrix)):
        matrix[i][i], matrix[i][-i - 1] = matrix[i][-i - 1], matrix[i][i]

    return matrix


def main() -> None:
    size = int(input())

    table = []

    for i in range(size):
        row = []
        user_input = [int(i) for i in input().split(",")]
        for j in range(size):
            row.append(user_input[j])
        table.append(row)

    sum_diagonal = sum_diagonals(table)
    for i in revers_diagonal(table):
        print(*i)

    print(sum_diagonal)


table = [[]]

main()
