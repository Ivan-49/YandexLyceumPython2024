numbers = [int(i) for i in input().split()]

max_len = max(numbers) + 1

itog = (
    [(max_len + 1) * "*"]
    + ["*" + (n * "*").rjust(max_len, " ") for n in numbers]
    + [(max_len + 1) * "*"]
)

for i in range(max_len + 1):
    print("".join(itog[j][i] for j in range(len(itog))))
