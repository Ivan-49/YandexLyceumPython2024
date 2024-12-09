list_ = [input() for _ in range(int(input()))]
words = [input() for _ in range(int(input()))]
count = len(words)
for string in list_:
    count = len(words)
    for word in words:
        if word in string:
            count -= 1
    if count == 0:
        print(string)
