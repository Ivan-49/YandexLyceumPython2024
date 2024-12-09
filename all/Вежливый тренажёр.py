name = input("Назовите себя, пожалуйста!\n")
text1 = input("Введите текст.\n")
text2 = input("Повторите текст.\n")
if text1 == text2:
    print(f"{name}, введено верно!")
else:
    print(f"{name}, пока не получилось, попробуйте снова!")
