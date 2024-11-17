rooms = {
    "Вход": {
        "description": "Вы находитесь у входа в лабиринт.",
        "connections": {"север": "Коридор"}
    },
    "Коридор": {
        "description": "Длинный коридор с дверями по обеим сторонам.",
        "connections": {"юг": "Вход", "восток": "Комната с сокровищами", "север": "Выход"}
    },
    "Комната с сокровищами": {
        "description": "Вы нашли комнату, полную сокровищ!",
        "connections": {"запад": "Коридор"}
    },
    "Выход": {
        "description": "Вы видите дверь на выход. Свобода ждет!",
        "connections": {"юг": "Коридор"}
    }
}

room = "Вход"

while True:
    print(rooms[room]["description"])
    directions = ", ".join(rooms[room]["connections"].keys())
    print(f"Вы можете двигаться: {directions}")
    command = input("Введите команду ([направление] или quit): ").strip().lower()

    if command in rooms[room]["connections"]:
        room = rooms[room]["connections"][command]
    elif command == "quit":
        print("Спасибо за игру!")
        break
    else:
        print("Неизвестная команда.")

