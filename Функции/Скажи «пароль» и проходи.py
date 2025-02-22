def ask_password():

    for i in range(3):
        password = input()
        if password == "password":
            print("Пароль принят")
            return
    print("В доступе отказано")
