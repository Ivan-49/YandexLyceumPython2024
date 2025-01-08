numbers = [[int(j) for j in input().split()] for i in range(int(input()))]


def median(numbers):
    result = []
    for i in numbers:
        result.append(sorted(i)[len(i) // 2])

    return result


def mode(numbers):
    res = []
    # numbers = sorted(num/bers)
    for strings in numbers:
        result = {}
        for i in strings:
            if i not in result.keys():
                result[i] = strings.count(i)
        res.append(max(result, key=result.get))
    return res


def median_of_medians(numbers):
    return median([median(numbers)])


def mode_of_modes(numbers):
    return mode([mode(numbers)])


def median_all(numbers):
    all = []
    for i in numbers:
        for j in i:
            all.append(j)

    return median([all])


def mode_all(numbers):
    all = []
    for i in numbers:
        for j in i:
            all.append(j)

    return mode([all])


if __name__ == "__main__":
    print(*median(numbers))
    print(*mode(numbers))
    print(*median_of_medians(numbers))
    print(*mode_of_modes(numbers))
    print(*median_all(numbers))
    print(*mode_all(numbers))
