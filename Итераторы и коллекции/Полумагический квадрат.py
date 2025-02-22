from sys import stdin


input_data = stdin.readlines()

matrix1 = []
matrix2 = []

for line in input_data:
    matrix1.append(list(map(int, line.split())))

for i in range(len(matrix1[0])):
    matrix2.append([row[i] for row in matrix1])

a = sum(matrix1[0])

for row in matrix1:
    if sum(row) != a:
        print("NO")
        exit()

for row in matrix2:
    if sum(row) != a:
        print("NO")
        exit()

print("YES")
