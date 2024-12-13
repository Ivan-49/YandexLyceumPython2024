strings = [input() for i in range(int(input()))]

for i in strings:
    if i[:2] == '%%':
        print(i[2:])
    elif i[:4] == '####':
        pass
    else:
        print(i)