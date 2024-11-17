def sum_steps(n: int) -> int:
    res = 0
    for i in range(1, n + 1):
        a = 0
        if i % 2 == 0:
            for j in range(2, i + 1, 2):
                a += j
        if i % 2 == 1:
            for j in range(1, i + 1, 2):
                a += j
        res += i**a
    return res


def main() -> None:
    user_num = int(input())
    res = sum_steps(user_num)
    print(res)


if __name__ == "__main__":
    main()
