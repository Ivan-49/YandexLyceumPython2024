height_borya = int(input())
height_vova = int(input())
height_dima = int(input())

heights = [height_borya, height_vova, height_dima]
heights.sort(reverse=True)

for height in heights:
    print(height)
