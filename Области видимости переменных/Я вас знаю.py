name = ""


def polite_input(question):
    global name
    if not name:
        name = input("Как вас зовут?\n")
    print(f"{name}, {question}")
    return input()
