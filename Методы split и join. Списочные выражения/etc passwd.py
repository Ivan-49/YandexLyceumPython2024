user = input()
users = []

while user:
    user = user.split(':')
    print(user)
    user_a = {
        'login':user[0],
        'password':user[1],
        'number':user[2],
        'number_group':user[3],
        'desciption':user[4],
        'home_dir':user[5],
        'shell':user[6]
    }
    users.append(user_a)
    user = input()
    


passwords = input().split(';')

for user in users:
    if user['password'] in passwords:
        print('To:' + user['login'])
        print(user['desciption'].split(', ')[0]+ ', ваш пароль слишком простой, смените его.')