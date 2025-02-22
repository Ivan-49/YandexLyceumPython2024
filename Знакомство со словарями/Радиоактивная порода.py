elements = [x for x in input().split()]
pairs = [(elements[i * 2], int(elements[i * 2 + 1])) for i in range(len(elements) // 2)]
decay_dict = {}
main_decay = dict(pairs)
current_decay = main_decay.copy()

key_sequence = [x for x in input().split()]
for key in key_sequence:
    if key not in decay_dict:
        decay_dict[key] = []

decay_values = [float(x) for x in input().split()]

for i, key in enumerate(key_sequence):
    if [] not in decay_dict[key]:
        decay_dict[key].append([])

    decay_dict[key][decay_dict[key].index([])].append(decay_values[i])

total_decay = float(input())
gcd = int(list(main_decay.values())[0])

for value in list(main_decay.values())[1:]:
    a, b = gcd, value
    while a != 0:
        a, b = b % a, a
    gcd = b

current_time = 0

while total_decay < sum(sum(sum(list(decay_dict.values()), []), [])):
    current_time += gcd
    for key in main_decay.keys():
        if not current_time % main_decay[key] and key in decay_dict:
            for i in range(len(decay_dict[key])):
                for j in range(len(decay_dict[key][i])):
                    decay_dict[key][i][j] /= 2

results = []

for key in key_sequence:
    results.append(decay_dict[key][0][0])
    del decay_dict[key][0]

print(current_time)
print(" ".join(map(str, results)))
