word = input()
num = int(input())
if len(word) >= num and num > 0:
    print(word[num - 1])
else:
    print("ОШИБКА")
