[
    print(list(i.keys())[0], list(i.values())[0])
    for i in (
        reversed(
            sorted(
                [{input(): int(input())} for i in range(int(input()))],
                key=lambda x: x.keys(),
            )
        )
    )
]
