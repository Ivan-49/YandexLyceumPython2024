num_items = int(input())
items = []
for _ in range(num_items):
    height = int(input())
    probability = float(input())
    items.append((height, probability))

for i in range(num_items):
    for j in range(i + 1, num_items):
        if items[j][0] > items[i][0] or (items[j][0] == items[i][0] and items[j][1] > items[i][1]):
            items[i], items[j] = items[j], items[i]

for item in items:
    print(item)
