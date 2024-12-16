glas = ["а", "е", "и", "о", "у", "ы", "э", "ю", "я", "ё"]
not_glas = [
    "б",
    "в",
    "г",
    "д",
    "ж",
    "з",
    "й",
    "к",
    "л",
    "м",
    "н",
    "п",
    "р",
    "с",
    "т",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ь",
]

tamplate = input()
words = []
user = input()


while user:

    words.append(user)
    user = input()

result = []
for word in words:
    res = ""

    if "*" in tamplate:
        if len(word) < len(tamplate) - 1:
            continue
    else:
        if len(word) != len(tamplate):
            continue

    if "*" not in tamplate:
        for i in range(len(word)):
            match tamplate[i]:
                case "1":
                    if word[i] in not_glas:
                        res += word[i]
                case "0":
                    if word[i] in glas:
                        res += word[i]
                case "?":
                    if (word[i] in glas) or (word[i] in not_glas):
                        res += word[i]
    else:
        tamplate = tamplate.split("*")
        res1, res2 = "", ""
        count_nach, count_kon = 0, 0
        for j in range(len(tamplate[0])):

            match tamplate[0][j]:
                case "1":
                    if word[j] in not_glas:
                        res1 += word[j]
                case "0":
                    if word[j] in glas:
                        res1 += word[j]
                case "?":
                    if (word[j] in glas) or (word[j] in not_glas):
                        res1 += word[j]
            count_nach += 1

        for k in range(1, len(tamplate[1]) + 1):
            match tamplate[1][-k]:
                case "1":
                    if word[-k] in not_glas:
                        res2 += word[-k]
                case "0":
                    if word[-k] in glas:
                        res2 += word[-k]
                case "?":
                    if (word[-k] in glas) or (word[-k] in not_glas):
                        res2 += word[-k]
            count_kon += 1
        if not (len(res1) + len(res2) == len(word)):
            
            res3 = word[count_nach:-count_kon]
            if count_kon == 0:
                res3 = word[count_nach:]
        else:
            res3 = ""

        res = res1 + res3 + "".join(reversed(res2))
        tamplate = "*".join(tamplate)
    if res == word:
        result.append(res)
print(*result, sep="\n") if result else print("Есть нечего, значить!")
