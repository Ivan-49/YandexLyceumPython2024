last_names = [input() for _ in range(int(input()))]
print(sum([1 for i in last_names if last_names.count(i) > 1]))
