class Person:
    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month

    def get_to_month(month):
        result = []
        for person in persons:
            if person.month == month:
                result.append(person)
        result.sort(key=lambda x: (int(x.day), x.name))

        return result


persons = []
for i in range(int(input())):
    name, day, month = input().split()
    person = Person(name, day, month)
    persons.append(person)
for i in range(int(input())):
    prores = []
    for i in Person.get_to_month(input()):
        prores.append(i.name)
        prores.append(i.day)
    print(*prores, sep=" ")
