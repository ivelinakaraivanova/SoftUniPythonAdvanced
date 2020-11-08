size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(size):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][size - i - 1]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
