user = input()
last = ""
kind = 0
mad = 0
while user != "":
    if user == "добрый":
        kind += 1
        last = "добрый"
    elif user == "злой":
        mad += 1
        last = "злой"
    elif user == "Какой подарок?":
        if kind > mad and last == "добрый":
            print("серебряный шиллинг")
        elif mad > kind and last == "злой":
            print("золотой")
        else:
            print("Ах, не знаю!")
            break
        last = ""
        kind = 0
        mad = 0
    else:
        break
    user = input()
