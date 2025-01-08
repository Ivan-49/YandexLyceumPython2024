from types import NoneType

COUNT_ROUNDS: int = int(input())  # количество раундов

user_strings: list[str] = [
    [int(j) for j in input().split()] for _ in range(COUNT_ROUNDS)
]  # пользователь вводит строки


for string in user_strings:

    result: list[str] = []  # результат

    while string:
        if max(string) == string[0]:
            result.append(string.pop(0))

        elif max(string) == string[-1]:
            result.append(string.pop(-1))

        else:
            result = ["НЕТ"]
            break

    print(*result, sep=" ")
