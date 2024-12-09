list_ = [input() for _ in range(int(input()))]
word = int(input())
res = ""
for i in list_:
    if word <= len(i):
        res += i[word - 1]
print(res)
