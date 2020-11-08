def is_valid(position, size):
    row, col = position
    return 0 <= row < size and 0 <= col < size


def get_attacked_count(matrix, r, c, size):
    attacked_knights = 0
    rows = [-1, 1, -2, 2, -1, 1, -2, 2]
    cols = [2, 2, 1, 1, -2, -2, -1, -1]
    for i in range(8):
        current_position = [r + rows[i], c + cols[i]]
        if is_valid(current_position, size) and matrix[current_position[0]][current_position[1]] == "K":
            attacked_knights += 1
    return attacked_knights


n = int(input())
board = [[x for x in input()] for _ in range(n)]

total_killed = 0

while True:
    max_killed = 0
    to_kill = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == "K":
                attacked_knights = get_attacked_count(board, i, j, n)
                if attacked_knights > max_killed:
                    max_killed = attacked_knights
                    to_kill = [i, j]

    if max_killed == 0:
        break

    to_kill_row, to_kill_col = to_kill
    board[to_kill_row][to_kill_col] = '0'
    total_killed += 1

print(total_killed)