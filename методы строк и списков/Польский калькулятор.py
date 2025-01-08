input_tokens = input().split()
numbers_stack = []

for token in input_tokens:
    if token == "+":
        operand2 = numbers_stack[0]
        operand1 = numbers_stack[1]
        result = int(operand1) + int(operand2)
        numbers_stack = [result] + numbers_stack[2:]
    elif token == "-":
        operand2 = numbers_stack[0]
        operand1 = numbers_stack[1]
        result = int(operand1) - int(operand2)
        numbers_stack = [result] + numbers_stack[2:]
    elif token == "*":
        operand2 = numbers_stack[0]
        operand1 = numbers_stack[1]
        result = int(operand1) * int(operand2)
        numbers_stack = [result] + numbers_stack[2:]
    elif token == "/":
        operand2 = numbers_stack[0]
        operand1 = numbers_stack[1]
        result = int(operand1) // int(operand2)
        numbers_stack = [result] + numbers_stack[2:]
    else:
        numbers_stack = [token] + numbers_stack

print(numbers_stack[0])
