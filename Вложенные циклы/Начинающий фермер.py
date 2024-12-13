credit = int(input())
heads = int(input())
for i in range(1, min(heads, credit // 20) + 1):
    for j in range(0, min(heads, credit // 10) + 1):
        for _ in range(0, min(heads, credit // 5) + 1):
            if (i * 20 + j * 10 + _ * 5 == credit) and (i + j + _ == heads):
                print(i, j, _)
