n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
m = len(matrix)

while True:
    token = input().split()
    command = token[0]
    if command == "END":
        break
    else:
        row = int(token[1])
        col = int(token[2])
        value = int(token[3])
        if 0 <= row < n and 0 <= col < m:
            if command == "Add":
                matrix[row][col] += value
            elif command == "Subtract":
                matrix[row][col] -= value
        else:
            print("Invalid coordinates")


[print(" ".join([str(x) for x in row])) for row in matrix]
