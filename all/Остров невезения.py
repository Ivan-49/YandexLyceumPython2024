def calculate_weekday(d, m, y):
    if m < 3:
        m += 12
        y -= 1
    y_century = y // 100
    y_year = y % 100
    day_of_week = (
        d
        + (13 * (m + 1) // 5)
        + y_year
        + (y_year // 4)
        + (y_century // 4)
        - 2 * y_century
    ) % 7
    return day_of_week


d = int(input().strip())
m = int(input().strip())
y = int(input().strip())

result = calculate_weekday(d, m, y)

result = (result + 6) % 7
print(result)
