def print_statistics(arr):
    """
    функция принимает список, выводит:
    1)число элементов
    2)среднее значение
    3)минимальное значение
    4)максимальное значение
    5)медиану списка
    """
    arr = list(map(float, arr))
    if len(arr) == 0:
        for i in range(5):
            print(0)
        return
    print(len(arr))
    print(sum(arr) / len(arr))
    print(min(arr))
    print(max(arr))
    if len(arr) % 2 == 1:
        print(sorted(arr)[len(arr) // 2])
    else:
        print((sorted(arr)[len(arr) // 2] + sorted(arr)[len(arr) // 2 - 1]) / 2)
