def month_name(month_number, language):
    """
    Возвращает название месяца на указанном языке.

    Args:
        month_number: Номер месяца (1-12).
        language: Язык ("en" для английского, "ru" для русского).

    Returns:
        Название месяца строкой, или "Invalid month number" если номер месяца некорректный.
    """
    months_en = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    months_ru = {
        1: "январь",
        2: "февраль",
        3: "март",
        4: "апрель",
        5: "май",
        6: "июнь",
        7: "июль",
        8: "август",
        9: "сентябрь",
        10: "октябрь",
        11: "ноябрь",
        12: "декабрь",
    }

    if not 1 <= month_number <= 12:
        return "Invalid month number"

    if language == "en":
        return months_en[month_number]
    elif language == "ru":
        return months_ru[month_number]
