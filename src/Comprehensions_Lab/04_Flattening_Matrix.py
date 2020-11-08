n = int(input())
matrix = [[int(x) for x in input().split(',')] for _ in range(n)]
flat_matrix = [num for row in matrix for num in row]
print(flat_matrix)