def check_win(row: list) -> bool:
    count = 0
    old = ""
    new = ""
    for i in row:
        if i == old:
            count += 1
        else:
            old = i
            new = i
            count = 1
        if count == 3:
            if new == ".":
                return
            return new


def main() -> None:
    aaaaaaa = []
    playng_field = int(input())
    for i in range(playng_field):
        row = [_ for _ in input()]
        aaaaaaa.append(row)

    for i in aaaaaaa:
        if check_win(i):
            print(check_win(i))
            exit()

    for i in range(len(aaaaaaa)):
        a = [aaaaaaa[j][i] for j in range(len(aaaaaaa))]
        if check_win(a):
            print(check_win(a))
            exit()
    print("-")


if __name__ == "__main__":
    main()
