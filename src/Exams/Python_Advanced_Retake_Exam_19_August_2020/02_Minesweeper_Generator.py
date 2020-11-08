def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_mines_around(matrix, r, c, size):
    count = 0
    rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        current_position = [r + rows[i], c + cols[i]]
        if is_valid(current_position[0], current_position[1], size) \
                and matrix[current_position[0]][current_position[1]] == "*":
            matrix[r][c] += 1
    return matrix[r][c]


size = int(input())
mines_number = int(input())
field = [[0 for _ in range(size)] for _ in range(size)]

for i in range(mines_number):
    line = input().lstrip("(").rstrip(")")
    split_line = line.split(", ")
    row_mine = int(split_line[0])
    col_mine = int(split_line[1])
    field[row_mine][col_mine] = '*'

for r in range(size):
    for c in range(size):
        if field[r][c] != "*":
            field[r][c] = get_mines_around(field, r, c, size)

for row in field:
    print(" ". join(str(x) for x in row))