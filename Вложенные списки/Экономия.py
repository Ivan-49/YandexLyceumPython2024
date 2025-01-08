def find_optimal_station(n, distances, start_a, start_a1):

    min_distance = distances[max(start_a, start_a1)][
        min(start_a, start_a1)
    ]  # из-за ошибок, при вводе size=1, будет ошибка

    optimal_station = -1

    for i in range(n):
        if i != start_a and i != start_a1:
            current_distance = (
                distances[max(start_a, i)][min(start_a, i)]
                + distances[max(i, start_a1)][min(i, start_a1)]
            )
            if current_distance < min_distance:
                min_distance = current_distance
                optimal_station = i

    return optimal_station if optimal_station != -1 else start_a


if __name__ == "__main__":
    n = int(input())

    distances = [[0] * n for _ in range(n)]
    for i in range(1, n):
        row_input = input().split()

        distances[i] = [int(x) for x in row_input]

    station = input().split()
    start_a, start_a1 = int(station[0]), int(station[1])

    result = find_optimal_station(n, distances, start_a, start_a1)
    print(result)
