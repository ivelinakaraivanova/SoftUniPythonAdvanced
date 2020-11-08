def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_start(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'P':
                return [r, c]


def move(command, row, col, size):
    is_punished = False
    new_row = row
    new_col = col

    if command == "up":
        new_row -= 1
    elif command == 'down':
        new_row += 1
    elif command == "left":
        new_col -= 1
    elif command == "right":
        new_col += 1

    if not is_valid(new_row, new_col, size):
        is_punished = True
        return [row, col], is_punished
    return [new_row, new_col], is_punished



initial_string = input()
size = int(input())
field = [[x for x in input()] for _ in range(size)]

start_position = get_start(field, size)
row_index, col_index = start_position
field[start_position[0]][start_position[1]] = "-"

command_number = int(input())

for _ in range(command_number):
    command = input()
    moved_idxs, for_punishment = move(command, row_index, col_index, size)
    row_index, col_index = moved_idxs

    if for_punishment:
        if len(initial_string) > 0:
            initial_string = initial_string[:-1]
    else:
        if field[row_index][col_index] != "-":
            initial_string += field[row_index][col_index]

        field[row_index][col_index] = '-'

field[row_index][col_index] = "P"

print(initial_string)

for row in field:
    print("".join([x for x in row]))
