img = []
height = int(input())
width = int(input())
for i in range(height):
    img.append(input())

for idex, val in enumerate(img): 
    if idex % 2 == 0:
        print(val[::2])
