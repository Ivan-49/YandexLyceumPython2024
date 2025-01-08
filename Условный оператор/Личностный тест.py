answers = [input() for i in range(2)]
if (not (answers[0] in ["да", "нет"])) or (not (answers[1] in ["да", "нет"])):
    print("Вы ввели неправильные данные")
else:
    match answers:
        case ["да", "да"]:
            print("вы нам подходите")
        case ["нет", "нет"]:
            print("мы вам перезвоним")
        case ["да", "нет"]:
            print("хорошо, думаю мы можем попробовать взять вас на работу")
        case ["нет", "да"]:
            print("это конечно так себе")
