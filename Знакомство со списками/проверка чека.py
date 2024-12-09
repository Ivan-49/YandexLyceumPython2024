result = []
count, sum_ = tuple(map(int, input().split()))
receipt = [tuple(input().split()) for i in range(count)]
true_sum = sum([int(i[0]) * int(i[1][1:]) for i in receipt])
print(sum_ - true_sum)
for i in receipt:
    if int(i[0]) * int(i[1][1:]) != int(i[2][1:]):
        result.append(receipt.index(i) + 1)

print(*result, sep=" ")
