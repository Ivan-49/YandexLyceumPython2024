first = input()
second = input()    

if first[-1] == second[0] or (first[-1] == "ь" and second[0] == first[-2]):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")