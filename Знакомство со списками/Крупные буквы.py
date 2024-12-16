chrs = {
    "a": [" * ", "* *", "***", "* *", "* *"],
    "b": ["** ", "* *", "** ", "* *", "** "],
    "c": [" * ", "* *", "*  ", "* *", " * "],
}

res = ["", "", "", "", ""]

user = input().lower()

for j in range(5):
    for i in user:
        res[j] += chrs[i][j] + "  "

[print(i) for i in res]
