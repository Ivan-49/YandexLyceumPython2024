list_ = []
for i in range(int(input())):
    a = []
    for _ in range(int(input())):
        a.append(input())
    list_.append(set(a))

print(*set.intersection(*list_), sep="\n")
