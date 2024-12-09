count_ctones = int(input())
while True:
    if count_ctones % 2 == 1:
        deductible = 1
        count_ctones -= deductible
        print(deductible, count_ctones)
    elif count_ctones % 2 != 0:
        deductible = 3
        count_ctones -= deductible
        print(deductible, count_ctones)
    elif count_ctones % 2 != 0 and count_ctones < 3:
        deductible = 1
        count_ctones -= deductible
        print(deductible, count_ctones)
    elif count_ctones == 2:
        deductible = 2
        count_ctones = 0
        print(deductible, count_ctones)
    if count_ctones == 0:
        print("Вы выиграли!")
        break
    user = int(input())
    if user > 3 or user < 1:
        print("Некорректный ход:", user)
    else:
        count_ctones -= user
        print(user, count_ctones)
        if count_ctones == 0:
            print("ИИ выиграл!")
            break
