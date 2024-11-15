number = int(input())
if 100 <= number <= 999:
    a = number // 100          
    b = (number // 10) % 10    
    c = number % 10            
    max_digit = max(a, b, c)
    min_digit = min(a, b, c)
    half_sum = (max_digit + min_digit) / 2
    if half_sum == (a + b + c - max_digit - min_digit):
        print("Вы ввели красивое число")
    else:
        print("Жаль, вы ввели обычное число")
else:
    print("Число должно быть трехзначным.")