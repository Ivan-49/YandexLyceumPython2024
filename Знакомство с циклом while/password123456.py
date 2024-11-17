password1 = input()


if len(password1) >= 8:
    if not ('123' in password1):
        password2 = input()
        if password1 == password2:
            print('OK')
        else:
            print("Различаются.")
    else:
        print("Простой!")
else:
    print("Короткий!") 	