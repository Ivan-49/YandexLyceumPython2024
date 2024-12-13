for i in range(1, int(input()) + 1):
    for j in range(i - 1, -1, -1):
        print(f"Осталось секунд: {j}")
    print(f"Пуск {i}")
