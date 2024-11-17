print(
    *(
        lambda m, n: [
            " ".join(str((j + 1) / (i + 1)) for j in range(m)) for i in range(n)
        ]
    )(int(input()), int(input())),
    sep="\n"
)
