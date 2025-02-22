def prediction(*args, **kwargs) -> dict:
    factor = 2 if kwargs.get("factor") is None else kwargs.get("factor")

    result = {}

    for i in args:
        if len(i) % factor != 0:
            continue
        if "letter" in kwargs.keys():
            letter = kwargs["letter"]
            if i[0] == letter:
                continue
        if len(i) not in result.keys():
            result[len(i)] = []
        result[len(i)].append(i)
    if "func" in kwargs.keys():
        func = kwargs["func"]
        for i in result.keys():
            result[i] = sorted(result[i], key=func)

    return result


args = [
    "Tea",
    "predict",
    "future",
    "voice",
    "sounded",
    "calm",
    "Everyone",
    "knows",
    "that",
    "Except",
    "for",
    "the",
    "tea",
    "leaves",
    "themselves",
]
kwargs = {"letter": "t"}
print(prediction(*args, **kwargs))


args = [
    "You",
    "have",
    "completely",
    "imbecile",
    "try",
    "argue",
    "with",
    "Tea",
    "leaves",
]
kwargs = {"factor": 3, "func": str.lower}
print(prediction(*args, **kwargs))
