total_stones = int(input())
remaining_stones = total_stones

while remaining_stones > 0:
    stones_taken = int(input())
    if 1 <= stones_taken <= 3 and stones_taken <= remaining_stones:
        remaining_stones -= stones_taken
    print(remaining_stones)
