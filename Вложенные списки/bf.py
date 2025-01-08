code = input()
memory: list[int] = [0] * 30001
pointer: int = 0
index: int = 0
code_length = len(code)
bracket_map = {}
stack = []

for i, command in enumerate(code):
    if command == "[":
        stack.append(i)
    elif command == "]":
        start = stack.pop()
        bracket_map[start] = i
        bracket_map[i] = start

while index < code_length:
    command = code[index]

    if command == ">":
        pointer += 1
    elif command == "<":
        pointer -= 1
    elif command == ".":
        print(memory[pointer])
    elif command == "+":
        memory[pointer] = (memory[pointer] + 1) % 256
    elif command == "-":
        memory[pointer] = (memory[pointer] - 1) % 256
    elif command == "[":
        if memory[pointer] == 0:
            index = bracket_map[index]
    elif command == "]":
        if memory[pointer] != 0:
            index = bracket_map[index]

    index += 1
