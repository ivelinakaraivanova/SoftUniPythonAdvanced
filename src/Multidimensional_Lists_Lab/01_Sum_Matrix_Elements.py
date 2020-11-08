rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

matrix_sum = 0
for row in matrix:
    matrix_sum += sum(row)

print(matrix_sum)
print(matrix)
