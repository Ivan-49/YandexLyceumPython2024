result = ""
step = int(input())
user_string = input()
for i in user_string:
    if 1040 <= ord(i) <= 1103:
        if ord(i) + step > 1103:
            result += chr(ord(i) + step - 32)
            continue
        if ord(i) <= 1071:
            result += chr(ord(i) + step).upper()
            continue
        result += chr(ord(i) + step)
    else:
        result += i

print(result)
