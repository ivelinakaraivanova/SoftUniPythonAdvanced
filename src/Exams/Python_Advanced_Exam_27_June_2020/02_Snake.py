def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_symbol(matrix, size, symbol):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == symbol:
                return r, c


def move(command, row, col, size):
    if command == "up":
        row -= 1
    elif command == 'down':
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1
    return [row, col]


size = int(input())
field = [[x for x in input()] for _ in range(size)]

start_position = get_symbol(field, size, 'S')
row_index, col_index = start_position

food_eaten = 0
is_gone_out = False
is_food_enough = False

while True:
    command = input()
    if command == '':
        break
    else:
        field[row_index][col_index] = "."
        row_index, col_index = move(command, row_index, col_index, size)
        if not is_valid(row_index, col_index, size):
            is_gone_out = True
            break
        else:
            if field[row_index][col_index] == "*":
                field[row_index][col_index] = "S"
                food_eaten += 1
                if food_eaten == 10:
                    is_food_enough = True
                    break
            elif field[row_index][col_index] == "B":
                field[row_index][col_index] = "."
                row_index, col_index = get_symbol(field, size, 'B')
                field[row_index][col_index] = "S"
            else:
                field[row_index][col_index] = "S"


if is_gone_out:
    print("Game over!")
elif is_food_enough:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_eaten}")

for row in field:
    print("".join([x for x in row]))
