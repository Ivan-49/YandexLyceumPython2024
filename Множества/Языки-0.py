from typing import Set


def city() -> list:
    city_set: Set[str] = set()
    count_city: int = int(input())
    for i in range(count_city):
        city_set.add(input())
    user: str = input()
    if user in city_set:
        print("TRY ANOTHER")
    else:
        print("OK")
    return None


def bus() -> None:
    set_nums_1: Set[str] = set()
    set_nums_2: Set[str] = set()
    num_house: str = input()
    while num_house:
        set_nums_1.add(num_house)
        num_house = input()
    num_house = input()
    while num_house:
        set_nums_2.add(num_house)
        num_house = input()
    res = set_nums_1 & set_nums_2
    if res:
        print(*res)
    else:
        print("EMPTY")


def language_0() -> None:
    english = set()
    german = set()
    english_count = int(input())
    german_count = int(input())

    for i in range(english_count):
        english.add(input())
    for i in range(german_count):
        german.add(input())
    result = len(set(english | german) - english) + len(set(english | german) - german)
    if result:
        print(result)
    else:
        print("NO")


def language_1() -> None:
    all_students: Set[str] = set()
    buffer: Set[str] = set()
    english_count: int = int(input())
    german_count: int = int(input())
    for i in range(english_count + german_count):
        student = input()
        all_students.add(student)
        if student in buffer:
            all_students.remove(student)
        buffer.add(student)

    if all_students:
        print(len(all_students))
    else:
        print("NO")


def language_2() -> None:

    all_students: Set[str] = set()
    buffer: Set[str] = set()
    buffer2: Set[str] = set()

    english_count: int = int(input())
    german_count: int = int(input())
    france_count: int = int(input())
    for i in range(english_count + german_count + france_count):
        student = input()
        all_students.add(student)

        if (student in buffer) and (student in buffer2):
            all_students.remove(student)

        if student in buffer:
            buffer2.add(student)
        buffer.add(student)
    if all_students:
        print(len(all_students))
    else:
        print("NO")


def main() -> None:
    language_0()


if __name__ == "__main__":
    main()
