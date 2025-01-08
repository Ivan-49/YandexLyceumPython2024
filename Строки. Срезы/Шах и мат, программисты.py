str_ = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
nums = [str(i) for i in range(1, 10)]

size = int(input())

for c in range(size, 0, -1):
    for n in range(size):
        print(str_[n] + nums[c - 1], end=" ")
    print()
