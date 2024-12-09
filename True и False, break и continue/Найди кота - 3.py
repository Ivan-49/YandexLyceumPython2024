a = False
line = 0
while True:
    while a is False:
        text = input()
        line += 1
        kol = 0
        if "Кот" in text or "кот" in text:
            a = True
            kol += 1
            break
        elif "СТОП" in text:
            break
    if "СТОП" in text:
        break
    text2 = input()
    if "Кот" in text2 or "кот" in text2:
        kol += 1
        continue
    if "СТОП" in text2:
        break
if a:
    print(kol, line)
else:
    print(0, -1)
