strings = []
total_sum = 0
all_numbers_del_3 = []
max_sum_index = -1
min_last_num = float("inf")
min_last_num_index = -1
line_count = 0

while True:
    line = input()
    line_count += 1
    numbers = [int(x) for x in line.split("_")]
    if any(num > 1_000_000 for num in numbers):
        break

    current_sum = sum(numbers)
    total_sum += current_sum
    for num in numbers:
        if num % 3 == 0:
            all_numbers_del_3.append(num)
    if (
        max_sum_index == -1 or current_sum > sum(strings[max_sum_index - 1][0])
        if strings
        else current_sum > 0
    ):
        max_sum_index = line_count

    if numbers and numbers[-1] < min_last_num:
        min_last_num = numbers[-1]
        min_last_num_index = line_count
    strings.append((numbers, line_count))

average_del_3 = (
    sum(all_numbers_del_3) // len(all_numbers_del_3) if all_numbers_del_3 else 0
)
total_rest = total_sum % 13

result = {
    "largest": max_sum_index,
    "smallest": min_last_num_index,
    "average": average_del_3,
    "rest": total_rest,
}

print(result)
