def print_document(pages):
    for i in pages:
        if "Секретно" in i:
            print("Дальнейшие материалы засекречены")
            return
        else:
            print(i)

    print("Напечатано без купюр")
