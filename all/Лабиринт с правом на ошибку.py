print("Вы находитесь в таинственной комнате с тремя выходами.")
print(
    'Вы можете пойти "налево", "направо" или "прямо". Введите одно из слов в кавычках для выбора.'
)
while True:
    first_choice = input().strip().lower()
    if first_choice == "налево":
        print("Вы направились налево. Через некоторое время вы дошли до двух дверей.")
        print('Вы выберете "левую" или "правую"?')
        while True:
            second_choice = input().strip().lower()
            if second_choice == "левую":
                print(
                    "Вы открыли левую дверь и нашли сундук с сокровищами! Вы победили!"
                )
                break
            elif second_choice == "правую":
                print(
                    "Вы смело открыли правую дверь. ",
                    " Но за ней вас подстерегала большая подземная жаба, она проглотила вас !",
                )
                break
            else:
                print("Ошибка: неверный выбор. Попробуйте еще раз.")
        break
    elif first_choice == "направо":
        print("Вы пошли направо и нашли выход из лабиринта. Вы свободны!")
        break
    elif first_choice == "прямо":
        print(
            "Вы пошли прямо и попали в тупик. К сожалению, вы застряли здесь навсегда."
        )
        break
    else:
        print("Ошибка: неверный выбор. Попробуйте еще раз.")
