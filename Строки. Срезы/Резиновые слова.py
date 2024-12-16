input_string = input()
length = len(input_string)

if length % 2 == 0:
    half_length = length // 2
    for i in range(half_length):
        print(
            " " * (half_length - i - 1)
            + input_string[half_length - i - 1]
            + " " * i
            + " " * i
            + input_string[half_length + i]
        )
else:
    middle_index = (length + 1) // 2
    print(
        " " * ((length - 1) // 2)
        + input_string[middle_index - 1]
        + " " * ((length - 1) // 2)
    )
    for i in range(1, middle_index):
        print(
            " " * (middle_index - i - 1)
            + input_string[middle_index - i - 1]
            + " " * i
            + " " * (i - 1)
            + input_string[middle_index + i - 1]
        )
