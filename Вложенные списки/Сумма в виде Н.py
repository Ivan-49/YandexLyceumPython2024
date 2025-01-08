def ns_in_matrix(matrix: list[list[int]], size: int = 3, n: int = 0) -> int:

    result = []

    for i in range(size - 2):
        for j in range(size - 2):
            """
            элементы в матрице расположенные в виде Н
            101
            111
            101
            """
            N = sum(
                [
                    matrix[i][j],
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    matrix[i][j + 2],
                    matrix[i + 1][j],
                    matrix[i + 1][j + 1],
                    matrix[i + 1][j + 2],
                    matrix[i + 2][j],
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    matrix[i + 2][j + 2],
                ]
            )

            result.append(N)
    return result


def main() -> None:

    size = int(input())
    matrix = [[int(j) for j in input().split()] for i in range(size)]
    all_n_in_matrix = ns_in_matrix(matrix, size=size)

    print(max(all_n_in_matrix))


if __name__ == "__main__":
    main()
