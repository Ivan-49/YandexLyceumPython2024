count_char: set = set()
user = input().lower()
for i in user:
    if i != " ":
        count_char.add((i, user.count(i), ord(i)))
aa = []
for chr, count, num in count_char:
    if count == max(count_char, key=lambda x: x[1])[1]:
        aa.append(chr)

print(min(aa, key=ord))
