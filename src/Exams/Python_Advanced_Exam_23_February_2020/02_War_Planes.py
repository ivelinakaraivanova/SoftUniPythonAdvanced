def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_start(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'p':
                return [r, c]


def get_total_targets(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "t":
                count += 1
    return count


def get_new_position(command, row, col, size, steps):
    new_row = row
    new_col = col

    if command == "up":
        new_row -= steps
    elif command == 'down':
        new_row += steps
    elif command == "left":
        new_col -= steps
    elif command == "right":
        new_col += steps

    if not is_valid(new_row, new_col, size):
        return [row, col]
    return [new_row, new_col]


size = int(input())
field = [[x for x in input().split()] for _ in range(size)]

total_targets = get_total_targets(field)
start_position = get_start(field, size)
row_index, col_index = start_position
field[start_position[0]][start_position[1]] = "."
killed_targets = 0

command_number = int(input())

for _ in range(command_number):
    command, direction, steps = input().split()
    steps = int(steps)
    new_row_index, new_col_index = get_new_position(direction, row_index, col_index, size, steps)
    if new_row_index == row_index and new_col_index == col_index:
        continue
    if command == "move":
        if field[new_row_index][new_col_index] == ".":
            field[new_row_index][new_col_index] = "p"
            field[row_index][col_index] = "."
            row_index, col_index = new_row_index, new_col_index
    elif command == "shoot":
        if field[new_row_index][new_col_index] != 'x':
            if field[new_row_index][new_col_index] == "t":
                killed_targets += 1
            field[new_row_index][new_col_index] = "x"

        if killed_targets == total_targets:
            break

left_targets = total_targets - killed_targets

if left_targets == 0:
    print(f"Mission accomplished! All {total_targets} targets destroyed.")
else:
    print(f"Mission failed! {left_targets} targets left.")

for row in field:
    print(" ".join([x for x in row]))
