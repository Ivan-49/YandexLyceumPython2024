import string


table = str.maketrans("", "", string.punctuation)


strings = [[_.lower() for _ in (input().split())] for _ in range(int(input()))]

strings_a = []
for i in strings:
    for j in i:
        new_s = j.translate(table)
        strings_a.append(new_s.capitalize())

result = {}

for i in strings_a:
    if i not in result.keys():
        result[i] = strings_a.count(i)
result2 = []
for key, value in result.items():
    result2.append((key, value))


result3 = sorted(result2, key=lambda x: (-x[1], x[0]), reverse=True)

for i in range(1, len(result3) + 1):
    print(result3[-i][0])
