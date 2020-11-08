rows_count, columns_count = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows_count):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

columns_sum = [0] * columns_count

for row in range(rows_count):
    for column in range(columns_count):
        columns_sum[column] += matrix[row][column]

for s in columns_sum:
    print(s)
