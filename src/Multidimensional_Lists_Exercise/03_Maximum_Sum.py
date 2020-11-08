def get_submatrix_sum(matrix, row, col, size):
    the_sum = 0
    for r in range(row, row + size):
        for c in range(col, col + size):
            the_sum += matrix[r][c]
    return the_sum


def print_submatrix(matrix, row, col, size):
    for r in range(row, row + size):
        for c in range(col, col + size):
            print(matrix[r][c], end=" ")
        print()


rows_count, columns_count = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]

size = 3
best_position = (0, 0)
best_value = get_submatrix_sum(matrix, 0, 0, size)

for row in range(len(matrix) - size + 1):
    for column in range(len(matrix[row]) - size + 1):
        current_value = get_submatrix_sum(matrix, row, column, size)
        if best_value < current_value:
            best_value = current_value
            best_position = (row, column)

best_row, best_column = best_position

print(f'Sum = {best_value}')
print_submatrix(matrix, best_row, best_column, 3)

