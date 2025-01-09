def calculate_popularity(n):
    popularity = {}
    text = input().split()
    name = text[0]
    views = int(text[-1])
    popularity[name] = [None, views]
    for _ in range(n - 1):
        text = input().split()
        name = text[0]
        ref_name = text[4][:-1]
        views = int(text[-1])
        popularity[name] = [ref_name, views]
        current_name = name
        current_views = views
        while ref_name:
            current_name = ref_name
            ref_name = popularity[current_name][0]
            popularity[current_name][1] += current_views
    return popularity


def print_popularity(popularity):
    print(*[x[1] for x in popularity.values()], sep="\n")


if __name__ == "__main__":
    n = int(input())
    result = calculate_popularity(n)
    print_popularity(result)
