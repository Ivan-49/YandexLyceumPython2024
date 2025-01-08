milk_botle = [int(input()) for _ in range(int(input()))]

min_ = int(input())
max_ = int(input())

[print(i) for i in milk_botle if min_ <= i <= max_]
