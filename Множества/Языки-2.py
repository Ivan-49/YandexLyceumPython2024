eng = int(input())
german = int(input())
france = int(input())
two_lang = 0
students = set()
students_two_languages = set()

for _ in range(eng + german + france):
    student_name = input()
    if student_name in students_two_languages:
        two_lang += 1
    elif student_name in students:
        students_two_languages.add(student_name)
    else:
        students.add(student_name)

count = eng + german + france - 2 * two_lang - len(students)

if count > 0:
    print(count)
else:
    print('NO')
