def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_symbol(matrix, size, symbol):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == symbol:
                return r, c


def get_queens(matrix, row, col, size, direction):
    result = []
    change_row = direction[0]
    change_col = direction[1]
    r = row
    c = col
    while is_valid(r, c, size):
        current_cell = matrix[r][c]
        if current_cell == "Q":
            result = [r, c]
            break

        r += change_row
        c += change_col

    return result


board = [[x for x in input().split()] for _ in range(8)]

king_row, king_col = get_symbol(board, 8, 'K')

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

queens = []
for d in directions:
    queen = get_queens(board, king_row, king_col, 8, d)
    if len(queen) > 0:
        queens.append(queen)

if len(queens) > 0:
    for q in queens:
        if len(q) > 0:
            print(q)
else:
    print("The king is safe!")
