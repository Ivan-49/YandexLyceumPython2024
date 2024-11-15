def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    year = int(input())
    result = "Високосный" if is_leap_year(year) else "Не високосный"
    print(result)

    
if __name__ == '__main__':
    main()