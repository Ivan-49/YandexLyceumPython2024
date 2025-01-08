def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def evaluate_rpn_expression(tokens):
    stack = []
    operations = {
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
        "*": lambda x, y: y * x,
        "/": lambda x, y: y // x,
        "~": lambda x: -x,
        "!": lambda x: factorial(x),
    }

    for token in tokens:
        if token in operations:
            if token in "+-*/":
                stack.append(operations[token](stack.pop(), stack.pop()))
            elif token in "~!":
                stack.append(operations[token](stack.pop()))
        elif token == "#":
            stack.append(stack[-1])
        elif token == "@":
            a, b, c = stack.pop(), stack.pop(), stack.pop()
            stack.extend([b, a, c])
        else:
            stack.append(int(token))

    return stack


if __name__ == "__main__":
    input_tokens = input().split()
    result_stack = evaluate_rpn_expression(input_tokens)
    print(*result_stack)
