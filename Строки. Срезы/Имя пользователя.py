import string


def create_char_list():
    lowercase_letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    underscore = "_"
    
    all_chars = lowercase_letters + digits + [underscore]
    return all_chars


def main():
    all_chars = create_char_list()
    
    for i in input():
        if i not in all_chars:
            print(f'Неверный символ: {i}')
            break
    else:
        print('OK')


if __name__ == "__main__":
    main()