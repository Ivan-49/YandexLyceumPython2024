while True:
    password1 = input()
    password2 = input()
    if len(password1) >= 8:
        if not ("123" in password1):
            if password1 == password2:
                print("OK")
                break
            else:
                print("Различаются.")
        else:
            print("Простой!")
    else:
        print("Короткий!")
