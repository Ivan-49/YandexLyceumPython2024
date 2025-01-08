a = input().split()
[print(len(i)) for i in a if len(i) == max(len(i) for i in a)]
