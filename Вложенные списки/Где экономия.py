n = int(input())
s = []


distances: list[list[int]] = [[0] * n for _ in range(n)]
for i in range(1, n):
    row_input: list[int] = list(map(int, input().split()))
    for j, cost in enumerate(row_input):
        distances[i][j] = distances[j][i] = cost

for start in range(n):
    for end in range(start + 1, n):
        shortest: int = distances[start][end]
        for point in range(n):
            if point != start and point != end:
                shortest = min(
                    shortest, distances[start][point] + distances[point][end]
                )
        if shortest != distances[start][end]:
            print(start, end)
