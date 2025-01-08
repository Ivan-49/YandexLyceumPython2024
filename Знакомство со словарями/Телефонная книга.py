numbers_book = {}
for _ in range(int(input())):
    number, name = input().split()
    if name not in numbers_book.keys():
        numbers_book[name] = number
    else:
        numbers_book[name] = numbers_book[name] + " " + number
for _ in range(int(input())):
    name = input()
    print(numbers_book.get(name, "Нет в телефонной книге"))
