while True:
    znac = int(input())
    if znac == 0:
        break
    elif znac % 3 == 0 and znac % 7 == 0:
        print("Караул!")
        break
    elif znac % 3 == 0:
        print("несчастливое")
    elif znac % 7 == 0:
        print("опасное")
    else:
        print(znac)