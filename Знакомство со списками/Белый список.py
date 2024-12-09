white_list = [input() for i in range(int(input()))]
requests = [input() for i in range(int(input()))]
result = []
for i in requests:
    if i in white_list:
        result.append(i)
for i in result:
    print(i)
