class User:
    def __init__(self, name, age, active, last_name, id):
        self.name = name
        self.age = age
        self.active = active
        self.last_name = last_name
        self.id = id

def id():
    i = 0
    while True:
        yield i
        i += 1
ids = id()

users = []
for i in range(int(input())):
    name = input()
    age = int(input())
    active = input()
    last_name = input()    
    users.append(User(name, age, active, last_name, ids.__next__())

for i in users:
    print(i.name, i.age, i.active, i.last_name, i.id)
