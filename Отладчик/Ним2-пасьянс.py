first_pile = int(input().strip())
second_pile = int(input().strip())

while True:
    pile_number = int(input().strip())
    stones_taken = int(input().strip())
    
    if pile_number == 1:
        first_pile -= stones_taken
    elif pile_number == 2:
        second_pile -= stones_taken
    
    print(first_pile, second_pile)
    
    if first_pile == 0 and second_pile == 0:
        break
