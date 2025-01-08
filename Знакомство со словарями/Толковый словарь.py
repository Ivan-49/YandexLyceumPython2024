dictory = {}

for i in range(int(input())):
    string_ = input().split()
    dictory[string_[0]] = " ".join(string_[1:])

for i in range(int(input())):
    word = input()
    print(dictory[word]) if word in dictory.keys() else print("Нет в словаре")
