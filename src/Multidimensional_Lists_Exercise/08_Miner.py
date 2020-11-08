def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_start(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 's':
                return [r, c]


def get_total_coals_count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "c":
                count += 1
    return count


def move(command, row, col, size):
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
        return [row, col]
    return [new_row, new_col]


n = int(input())
commands = input().split()
field = [[x for x in input().split()] for _ in range(n)]

total_coals = get_total_coals_count(field)
start_position = get_start(field, n)
row_index, col_index = start_position

is_total_coals = False
is_end = False

for command in commands:
    row_index, col_index = move(command, row_index, col_index, n)

    if field[row_index][col_index] == "c":
        total_coals -= 1
        field[row_index][col_index] = "*"
        if total_coals == 0:
            is_total_coals = True
            break

    elif field[row_index][col_index] == "e":
        is_end = True
        break

if is_total_coals:
    print(f"You collected all coals! ({row_index}, {col_index})")
elif is_end:
    print(f"Game over! ({row_index}, {col_index})")
else:
    print(f"{total_coals} coals left. ({row_index}, {col_index})")
