def treangle_of_pascal(len_: int = int(input()), row: list = [1]):
    print(*row)
    (
        treangle_of_pascal(
            len_, [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
        )
        if len(row) != len_
        else None
    )


treangle_of_pascal()
