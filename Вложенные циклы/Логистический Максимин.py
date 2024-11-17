num = int(input())
max_ = 0
road = 1
for element in range(num):
    tunnel = int(input())
    m = 100000000
    for element_2 in range(tunnel):
        height = int(input())
        if m > height:
            m = height
    if max_ < m:
        max_ = m
        road = element + 1
print(road, max_)