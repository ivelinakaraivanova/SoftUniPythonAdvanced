def swap_elements(matrix, row1, col1, row2, col2):
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    return matrix


rows_count, columns_count = [int(x) for x in input().split()]
input_matrix = [[x for x in input().split()] for _ in range(rows_count)]

is_invalid = False

while True:
    line = input()
    if line == "END":
        break
    else:
        command = line.split()

        if command[0] != "swap" or len(command) != 5:
            print("Invalid input!")
        else:
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            if r1 in range(rows_count) and r2 in range(rows_count) and c1 in range(columns_count) and c2 in range(columns_count):
                input_matrix = swap_elements(input_matrix, r1, c1, r2, c2)
                for row in input_matrix:
                    print(" ".join([str(x) for x in row]))
            else:
                print("Invalid input!")
