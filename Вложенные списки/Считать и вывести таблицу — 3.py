import sys
from typing import Iterator, List
import itertools
from typing import List


def fast_read_ints(n: int) -> Iterator[int]:
    return map(int, [next(sys.stdin.buffer).decode() for _ in range(n)])


def fast_read_lines_inner(n: int) -> List[str]:
    result = []
    for line in itertools.islice(sys.stdin.buffer, n):
        result.append(line.decode().strip())
    return result


def fast_read_lines(n: int) -> List[str]:
    return fast_read_lines_inner(n)


def main() -> None:
    try:
        num_rows, num_columns = fast_read_ints(2)
        if num_rows < 0 or num_columns < 0:
            raise ValueError("Размеры матрицы должны быть неотрицательными числами.")

        for _ in range(num_rows):
            print(*fast_read_lines(num_columns), sep="\t")

    except ValueError as e:
        print("Ошибка ввода:", e)
    except Exception as e:
        print("Неизвестная ошибка:", e)


if __name__ == "__main__":
    main()
