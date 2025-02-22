food = {}


def diet(eat_list: list):
    global food
    eat_list = eat_list.split()
    all_count = len(eat_list)
    count = 0
    for i in eat_list:
        if i in food.get("диетическое"):
            count += 1
    if (count * 2) > all_count:
        print("Не ешь столько, По!")
    else:
        print("Так держать, Воин Дракона!")
