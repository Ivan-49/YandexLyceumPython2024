list_ = [input() for _ in range(int(input()))]
word = input()
for i in list_:
    if word in i:
        print(i)
