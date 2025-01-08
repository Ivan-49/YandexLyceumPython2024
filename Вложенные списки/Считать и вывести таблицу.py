count_row = int(input())
count_column = int(input())
table = []
for i in range(count_row):
    all = []
    for i in range(count_column):
        all.append(input())
    table.append(all)

for count in range(count_column):
    max_ = 0
    for i in table:
        if max_ < len(i[count]):
            max_ = len(i[count])

    for i in table:
        if len(i[count]) < max_:
            i[count] += " " * (max_ - len(i[count]))

for i in table:
    print(*i)
