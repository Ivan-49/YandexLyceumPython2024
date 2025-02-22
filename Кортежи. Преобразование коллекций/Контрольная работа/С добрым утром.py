word = input()
user = input()

count_and_word = 0
count = 0

while "INSPECTOR" not in user:

    if word in user:
        count_and_word += 1

    count += 1
    user = input()

print(count_and_word / count)
