def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_start(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                return [r, c]


def get_eggs_up(matrix, row, col, size):
    the_sum = 0
    positions = []
    if get_start(matrix, size)[0] != 0:
        for r in range(row-1, -1, -1):
            current_egg = matrix[r][col]
            if current_egg == "X":
                break
            the_sum += int(matrix[r][col])
            positions.append([r, col])
    return the_sum, positions


def get_eggs_down(matrix, row, col, size):
    the_sum = 0
    positions = []
    if get_start(matrix, size)[0] != (size-1):
        for r in range(row+1, size):
            current_egg = matrix[r][col]
            if current_egg == "X":
                break
            the_sum += int(matrix[r][col])
            positions.append([r, col])
    return the_sum, positions


def get_eggs_left(matrix, row, col, size):
    the_sum = 0
    positions = []
    if get_start(matrix, size)[1] != 0:
        for c in range(col-1, -1, -1):
            current_egg = matrix[row][c]
            if current_egg == "X":
                break
            the_sum += int(matrix[row][c])
            positions.append([row, c])
    return the_sum, positions


def get_eggs_right(matrix, row, col, size):
    the_sum = 0
    positions = []
    if get_start(matrix, size)[1] != (size-1):
        for c in range(col+1, size):
            current_egg = matrix[row][c]
            if current_egg == "X":
                break
            the_sum += int(matrix[row][c])
            positions.append([row, c])
    return the_sum, positions


size = int(input())
field = [[x for x in input().split()] for _ in range(size)]

start_position = get_start(field, size)
row_index, col_index = start_position

sum_up = get_eggs_up(field, row_index, col_index, size)
sum_down = get_eggs_down(field, row_index, col_index, size)
sum_left = get_eggs_left(field, row_index, col_index, size)
sum_right = get_eggs_right(field, row_index, col_index, size)

max_sum = max(sum_up, sum_down, sum_left, sum_right)

direction = ''
if max_sum == sum_up:
    direction = "up"
elif max_sum == sum_down:
    direction = "down"
elif max_sum == sum_left:
    direction = "left"
elif max_sum == sum_right:
    direction = "right"
print(direction)

for item in max_sum[1]:
    print(item)

print(max_sum[0])
