def is_valid(position, size):
    row, col = position
    return 0 <= row < size and 0 <= col < size


def detonated_bomb(matrix, row, col, size):
    rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        current_position = [row + rows[i], col + cols[i]]
        if is_valid(current_position, size) and matrix[current_position[0]][current_position[1]] > 0:
            matrix[current_position[0]][current_position[1]] -= matrix[row][col]
    matrix[row][col] = 0
    return matrix


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = input().split()

for bomb in bombs:
    r, c = int(bomb.split(",")[0]), int(bomb.split(",")[1])
    if matrix[r][c] > 0:
        matrix = detonated_bomb(matrix, r, c, n)

alive_cells = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        cell = matrix[i][j]
        if cell > 0:
            alive_cells.append(cell)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(" ".join([str(x) for x in row]))
