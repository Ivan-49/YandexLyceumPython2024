from sys import stdin


bash_input = [i.strip().split() for i in stdin.readlines() if i.strip()]
top = {}
groups = {}
result = []

for i in bash_input:
    count = int(i[-1])
    count = count // 1000
    group = (round(count // 100) * 100, (round(count // 100) + 1) * 100)
    if groups.get(f"{group[0]} - {group[1]}") is None:
        groups[f"{group[0]} - {group[1]}"] = []
    groups[f"{group[0]} - {group[1]}"].append(i[0])


for i in groups:
    result.append(i + ": " + ", ".join(sorted(groups[i])))

result = sorted(result, key=lambda x: int(x.split()[0].split("-")[0]))

print(*result, sep="\n")
