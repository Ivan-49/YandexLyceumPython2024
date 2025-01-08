russian_letters_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
russian_letters_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
english_letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
english_letters_lower = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789_"

all_chars = (
    russian_letters_upper
    + russian_letters_lower
    + english_letters_upper
    + english_letters_lower
    + digits
)

logins = input().split(",")

printes = []

for i in logins:
    for char in i:
        if char not in all_chars:
            printes.append(i)
            break
if not printes:
    exit()
max_len = max(printes, key=len)

for i in sorted(printes):
    if i == max_len:
        print(i)
    else:
        print(i.rjust(len(max_len)))
