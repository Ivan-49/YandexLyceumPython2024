def make_shades(alley, k):
    length = len(alley)
    shades = [False] * length

    for i, height in enumerate(alley):
        if height > 0:
            if k > 0:
                start = i
                end = min(i + k * height, length - 1)
                for j in range(start, end + 1):
                    shades[j] = True
            elif k < 0:
                start = max(0, i + k * height)
                end = i
                for j in range(start, end + 1):
                    shades[j] = True
            else:
                shades[i] = True

    return shades


def calculate_sunny_length(shades):

    sunny_length = 0
    for shade in shades:
        if not shade:
            sunny_length += 1
    return sunny_length


def main():

    k = int(input())
    alley_str = input()
    alley = [int(h) for h in alley_str.split()]

    shades = make_shades(alley, k)
    sunny_length = calculate_sunny_length(shades)

    if sunny_length >= 10:
        print("Обгорел")
    else:
        print("Тени достаточно")


if __name__ == "__main__":
    main()
