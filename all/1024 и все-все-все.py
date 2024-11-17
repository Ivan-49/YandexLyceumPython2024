def is_power_of_two(n):
    if n < 1:
        return "НЕТ"
    power = 0 

    while (1 << power) < n:
        power += 1
    
    if (1 << power) == n:
        return power        
    else:
        return "НЕТ"


number = int(input())
result = is_power_of_two(number)
print(result)
