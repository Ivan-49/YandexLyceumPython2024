table = [input().split(",") for i in range(int(input()))]
cords = [tuple(input().split(",")) for i in range(int(input()))]

for row_num, column_num in cords:
    print(table[int(row_num)][int(column_num)])
