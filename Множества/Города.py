from typing import Set


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


def city() -> list:
    city_set: Set[str] = set()
    count_city = int(input())
    for i in range(count_city):
        city_set.add(input())
    user = input()
    if user in city_set:
        return True
    else:   
        return False
    return city_set


def main() -> None:    
    res = city() 
    match res:
        case True:
            print("TRY ANOTHER")
        case False:
            print("OK")


if __name__ == "__main__":
    main()
