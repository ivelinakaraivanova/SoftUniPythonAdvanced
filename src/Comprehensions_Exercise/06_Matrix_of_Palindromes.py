rows, cols = [int(x) for x in input(). split()]
matrix = [[0 for x in range(cols)] for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        matrix[r][c] = "" + chr(ord('a') + r) + chr(ord('a') + r + c) + chr(ord('a') + r)

for row in matrix:
    print(" ".join([str(x) for x in row]))
