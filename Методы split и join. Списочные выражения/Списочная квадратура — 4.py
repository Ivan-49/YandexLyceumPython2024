print(
    " ".join(
        [
            str(int(i) ** 2)
            for i in input().split()
            if int(i) % 2 == 1 and str(int(i[-1]) ** 2)[-1] != "9"
        ]
    )
)
