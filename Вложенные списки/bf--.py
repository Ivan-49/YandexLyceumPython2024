comand_line = input()

line = [0] * 30000
possition = 0

for commad in comand_line:
    match commad:
        case ">":
            possition = (possition + 1) % 30000
        case "<":
            possition = (possition - 1) % 30000
        case "+":
            if line[possition] == 255:
                line[possition] = 0
            else:
                line[possition] += 1
        case "-":
            if line[possition] == 0:
                line[possition] = 255
            else:
                line[possition] -= 1
        case ".":
            print(line[possition])
