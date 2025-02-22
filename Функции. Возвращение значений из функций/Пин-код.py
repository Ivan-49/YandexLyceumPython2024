def is_easy_num(num):
    return num in [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]


def num_is_polindrom(num):
    return str(num) == str(num)[::-1]


def num_is_prime(num):
    nums = [2**i for i in 1000]
    if num in nums:
        return True


def check_pin(pinCode):
    pinCode = list(map(int, pinCode.split("-")))
    if is_easy_num(pinCode[0]) and num_is_polindrom(pinCode[1]) and num_is_prime(pinCode[2]):
        print("Корректен")
    else:
        print("Некорректен")


