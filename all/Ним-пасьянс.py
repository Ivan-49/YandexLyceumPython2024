total_stones = int(input())

remaining_stones = total_stones

while remaining_stones > 0:
    stones_taken = int(input())
    if stones_taken <= 0 or stones_taken > remaining_stones:
        continue

    remaining_stones -= stones_taken

    print(remaining_stones)
