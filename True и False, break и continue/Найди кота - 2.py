cat = False
Cat = 0
a = input()
while a != 'СТОП':
    if not cat:
        Cat += 1 
    if 'КОТ' in a.upper():
        cat = True
    a = input()
if cat:
    print(Cat)
else:
    print(-1)
