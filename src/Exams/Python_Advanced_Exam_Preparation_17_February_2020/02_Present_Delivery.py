def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_start(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'S':
                return [r, c]


def get_total_nice_kids(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "V":
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


def get_neighbors(r, c, n):
    neighbors = [(r + a[0], c + a[1])
                 for a in [(0, -1), (0, 1), (-1, 0), (1, 0)]
                 if is_valid(r + a[0], c + a[1], n)]
    return neighbors


def count_presents(matrix, r, c):
    count = 0
    if matrix[r][c] == "V":
        count += 1
    elif matrix[r][c] == "C":
        neighbours = get_neighbors(r, c, size)
        for neighbour in neighbours:
            row, col = neighbour
            if neighbourhood[row][col] != "-":
                count += 1
                neighbourhood[row][col] = "-"
    return count


presents_count = int(input())
size = int(input())
neighbourhood = [[x for x in input().split()] for _ in range(size)]

total_nice_kids = get_total_nice_kids(neighbourhood)
start_position = get_start(neighbourhood, size)
row_index, col_index = start_position
is_total_presents = False
count_nice_kids = 0

neighbourhood[start_position[0]][start_position[1]] = "-"

while True:
    if is_total_presents:
        break
    else:
        command = input()
        if command == "Christmas morning":
            break
        else:
            row_index, col_index = move(command, row_index, col_index, size)

            presents_count -= count_presents(neighbourhood, row_index, col_index)
            if presents_count <= 0:
                is_total_presents = True
                break

            neighbourhood[row_index][col_index] = "-"

neighbourhood[row_index][col_index] = 'S'
left_count_nice_kids = get_total_nice_kids(neighbourhood)

if is_total_presents:
    if left_count_nice_kids > 0:
        print("Santa ran out of presents!")

for row in neighbourhood:
    print(" ".join([str(x) for x in row]))

if left_count_nice_kids == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
elif left_count_nice_kids > 0:
    print(f"No presents for {left_count_nice_kids} nice kid/s.")
