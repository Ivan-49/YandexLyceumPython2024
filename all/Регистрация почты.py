login = input()
adress = input()

if "@" in login:
    print("Некорректный логин")
elif not ("@" in adress):
    print("Некорректный адрес")
else:
    print("OK")
