index_ = [int(i) - 1 for i in input().split()]

text = input().split()
result = []
for i in index_:
    result.append(text[i].lower())

print(" ".join(result).capitalize())
