n = int(input())
even_matrix = [[int(x) for x in input().split(',') if int(x) % 2 == 0] for _ in range(n)]
print(even_matrix)

