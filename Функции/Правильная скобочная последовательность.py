def bracket_check(test_string):
    for i in test_string:
        if i not in "()":
            return False

    stack = []

    for char in test_string:
        match char:
            case "(":
                stack.append(char)

            case ")":
                if not stack:
                    print("NO")
                    return
                else:
                    del stack[-1]

    if not stack:
        print("YES")
    else:
        print("NO")
