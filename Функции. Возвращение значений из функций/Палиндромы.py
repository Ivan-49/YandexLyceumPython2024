def palindrome(s):

    return (
        "Палиндром"
        if "".join([i.lower() for i in s.split()])
        == "".join([i.lower() for i in s.split()])[::-1]
        else "Не палиндром"
    )
