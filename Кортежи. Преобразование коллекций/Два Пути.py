S = [int(input()) for i in range(int(input()))]

first = [*S]
second = [*S]

for i in range(int(input())):
    a = int(input())
    number = int(input())
    match a:
        case 1:
            first[number] = first[number] + int(input())
        case 2:
            second[number] = second[number] + int(input())
print(*first)
print(*second)
b = 0
for i in range(len(first)):
    if first[i] == second[i]:
        b += 1
print(b)
