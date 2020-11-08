def read_int_list_from_input(separator):
    return [int(x) for x in input().split(separator)]


def get_submatrix_sum(matrix, row, col):
    return matrix[row][col] + matrix[row+1][col] + matrix[row][col+1] + matrix[row+1][col+1]


def print_submatrix(matrix, row, col):
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            print(matrix[r][c], end=" ")
        print()


rows_count, columns_count = read_int_list_from_input(", ")
matrix = [read_int_list_from_input(", ") for _ in range(rows_count)]

best_position = (0, 0)
best_value = get_submatrix_sum(matrix, 0, 0)

for row in range(len(matrix) - 1):
    for column in range(len(matrix[row]) - 1):
        current_value = get_submatrix_sum(matrix, row, column)
        if best_value < current_value:
            best_value = current_value
            best_position = (row, column)

best_row, best_column = best_position
print_submatrix(matrix, best_row, best_column)
print(best_value)
