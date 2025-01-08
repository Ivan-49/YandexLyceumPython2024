user = input()
users_list = []

while user:
    user = user.split(":")
    user_data = {
        "login": user[0],
        "password": user[1],
        "number": user[2],
        "number_group": user[3],
        "desciption": user[4],
        "home_dir": user[5],
        "shell": user[6],
    }
    users_list.append(user_data)
    user = input()
passwords = input().split(";")
[
    print(
        f'To: {user['login']}\n{user["desciption"].split(
    ",")[0]}, ваш пароль слишком простой, смените его.'
    )
    for user in users_list
    if user["password"] in passwords
]
