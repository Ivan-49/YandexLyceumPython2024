def who_are_you_and_hello():
    while True:
        name = input()
        if (
            len(name.split()) == 1
            and name.isalpha()
            and name.capitalize() == name
            and name[1:].islower()
        ):
            print(f"Привет, {name}!")
            break
