def possible_turns(cell):
    def to_coords(s):
        return (ord(s[0]) - ord("A") + 1, int(s[1]))

    def to_cell(coords):
        return chr(ord("A") + coords[0] - 1) + str(coords[1])

    def valid(coords):
        return 1 <= coords[0] <= 8 and 1 <= coords[1] <= 8

    x, y = to_coords(cell)
    moves = [
        (x + 1, y + 2),
        (x + 1, y - 2),
        (x - 1, y + 2),
        (x - 1, y - 2),
        (x + 2, y + 1),
        (x + 2, y - 1),
        (x - 2, y + 1),
        (x - 2, y - 1),
    ]
    return sorted([to_cell(m) for m in moves if valid(m)])
