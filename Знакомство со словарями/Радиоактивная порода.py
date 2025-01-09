def calculate_decay(input_pairs, key_list, initial_values, normal_value):
    pairs = [
        (input_pairs[i * 2], int(input_pairs[i * 2 + 1]))
        for i in range(len(input_pairs) // 2)
    ]
    decay_rates = dict(pairs)
    value_dict = {key: [] for key in key_list}

    for i, key in enumerate(key_list):
        value_dict[key].append([initial_values[i]])

    gcd_val = list(decay_rates.values())[0]

    for val in list(decay_rates.values())[1:]:
        a, b = int(gcd_val), int(val)

        while a:
            a, b = b % a, a
        gcd_val = b

    time = 0

    total_sum = sum(sum(sum(value_dict.values(), []), []))

    while normal_value < total_sum:
        time += gcd_val

        for key, decay in decay_rates.items():
            if not time % decay and key in value_dict:
                for sublist in value_dict[key]:
                    for i in range(len(sublist)):
                        sublist[i] /= 2

        total_sum = sum(sum(sum(value_dict.values(), []), []))

    result_values = [value_dict[key][0][0] for key in key_list]

    return time, " ".join(map(str, result_values))


if __name__ == "__main__":

    input_pairs = input().split()
    key_list = input().split()
    initial_values = [float(x) for x in input().split()]
    normal_value = float(input())
    time, result = calculate_decay(input_pairs, key_list, initial_values, normal_value)

    print(time)
    print(result)
