tries = int(input())
counter = 0
countStr = ("раз", "два", "три", "четыре")
while tries > 0:
    i = 0
    while True:
        if input() != countStr[i]:
            print(
                "Правильных отсчётов было ", counter, ", но теперь вы ошиблись.", sep=""
            )
            counter = 0
            tries -= 1
            break
        counter += 1
        i = 0 if i == 3 else i + 1
print("На сегодня хватит.")
