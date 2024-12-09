temp = float(input())
count = 0
result = 0
while temp > -300:
    count += 1
    result += temp
    temp = float(input())
print(result / count)
