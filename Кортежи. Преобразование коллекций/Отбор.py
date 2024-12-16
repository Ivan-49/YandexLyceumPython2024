list_ = [tuple(input().split("\t")) for _ in range(int(input()))]
[print(*i, sep="\t") for i in list_]
print()
[print(*i, sep="\t") if int(i[1]) in [4, 5] else ... for i in list_]
