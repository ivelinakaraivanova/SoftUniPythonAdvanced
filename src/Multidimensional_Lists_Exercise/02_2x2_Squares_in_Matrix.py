def get_square_submatrix(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) - 1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                square = [
                    [matrix[i][j],matrix[i][j+1]],
                    [matrix[i+1][j],matrix[i+1][j+1]],
                ]
                squares.append(square)
    return squares


rows_count, columns_count = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows_count)]

square_matrix_count = len(get_square_submatrix(matrix))
print(square_matrix_count)
