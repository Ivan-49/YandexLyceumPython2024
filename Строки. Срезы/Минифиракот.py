def minify_code(lines):
    result = []
    for line in lines:
        leading_spaces = len(line) - len(line.lstrip())
        modified_line = line.lstrip()

        in_quotes = False
        escaped = False
        new_line = []

        for index, char in enumerate(modified_line):
            if char == "#" and not in_quotes:
                break

            if char == "'" and not escaped:
                in_quotes = not in_quotes

            if char == "\\" and not escaped:
                escaped = True
                new_line.append(char)
                continue

            if char == "\\" and escaped:
                escaped = False
                new_line.append(char)
                continue

            if char == " " and not in_quotes:
                if new_line and new_line[-1] == " ":
                    continue
                elif index == len(modified_line):
                    new_line.append(char)
                    continue
            else:
                escaped = False

            new_line.append(char)

        result.append(" " * leading_spaces + "".join(new_line))

    return result


n = int(input())
lines = [input() for _ in range(n)]

minified_lines = minify_code(lines)
for line in minified_lines:
    print(line)

