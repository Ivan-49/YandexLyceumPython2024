low = 1
high = 1000
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = (low + high) // 2 
    print(guess)
    response = input()

    if response == '=':
        break 
    elif response == '>':
        low = guess + 1 
    elif response == '<':
        high = guess - 1
    else:
        continue

    attempts += 1


