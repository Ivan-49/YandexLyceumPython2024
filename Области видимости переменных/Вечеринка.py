person_list = []


def add_friends(name_of_person, list_of_friends):
    global person_list
    if name_of_person in [i[0] for i in person_list]:
        for i in person_list:
            if i[0] == name_of_person:
                i[1].extend(list_of_friends)
                return
    person_list.append((name_of_person, list_of_friends))


def are_friends(name_of_person1, name_of_person2):
    global person_list
    for i in person_list:
        if i[0] == name_of_person1:
            if name_of_person2 in i[1]:
                return True
            else:
                return False


def print_friends(name_of_person):
    global person_list
    for i in person_list:
        if i[0] == name_of_person:
            print(*sorted(i[1]), sep=" ")
