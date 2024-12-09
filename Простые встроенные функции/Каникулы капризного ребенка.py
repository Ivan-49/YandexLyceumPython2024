non_valide_variable = [["Тула", "Тула"], ["Пенза", "Пенза"], ["Тула", "Пенза"]]
user = [input(), input()]
if not (user in non_valide_variable) and ((user[0] == "Тула") or (user[1] == "Пенза")):
    print("ДА")
else:
    print("НЕТ")
