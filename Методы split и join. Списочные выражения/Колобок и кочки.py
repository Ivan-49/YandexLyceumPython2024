num_words = int(input())
jumps = [int(input()) for _ in range(num_words)]
words = [input() for _ in range(num_words)]

answer = []

for i in range(num_words):
    word = words[i]
    jump = jumps[i]

    letter_counts = []
    for letter in word:
        found = False
        for j in range(len(letter_counts)):
            if letter_counts[j][0] == letter:
                letter_counts[j] = (letter_counts[j][0], letter_counts[j][1] + 1)
                found = True
                break
        if not found:
            letter_counts.append((letter, 1))

    found_letter = None
    for letter, count in letter_counts:
        if count == jump:
            if found_letter is not None:
                print("нечленораздельно")
                exit()
            found_letter = letter

    if found_letter is None:
        print("нечленораздельно")
        exit()

    answer.append(found_letter)
print("".join(answer))
