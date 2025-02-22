from itertools import permutations

dictionary = input().lower().split()
letter = input().lower().split()

for i in range(len(letter)):
    word = letter[i]
    sorted_word = "".join(sorted(word))

    for dict_word in dictionary:
        if word != dict_word and sorted_word == "".join(sorted(dict_word)):
            letter[i] = "#" * len(word)
            break

print(" ".join(letter))
