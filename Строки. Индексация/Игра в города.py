user: str = input()
last = user 
while True:
    user = input()
    if user[0] != last[-1]:
        print(user)
        break
    last = user