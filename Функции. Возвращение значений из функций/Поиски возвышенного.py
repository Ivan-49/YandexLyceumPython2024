def find_mountain(heightsMap):
    return max(
        ((i, j) for i, row in enumerate(heightsMap) for j, val in enumerate(row)),
        key=lambda x: heightsMap[x[0]][x[1]],
    )
