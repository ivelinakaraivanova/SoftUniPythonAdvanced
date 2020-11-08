n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
first_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if i == j]
second_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if i + j == n - 1]
print('First diagonal: ' + ', '.join(str(x) for x in first_diagonal) + '. Sum: ' + str(sum(first_diagonal)))
print('Second diagonal: ' + ', '.join(str(x) for x in second_diagonal) + '. Sum: ' + str(sum(second_diagonal)))
