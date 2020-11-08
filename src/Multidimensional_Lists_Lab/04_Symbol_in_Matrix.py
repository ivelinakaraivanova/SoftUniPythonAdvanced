size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)

symbol = input()
is_found = False
position = ()

for row in range(size):
    if is_found:
        break
    for column in range(size):
        if matrix[row][column] == symbol:
            position = (row, column)
            is_found = True

if is_found:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")