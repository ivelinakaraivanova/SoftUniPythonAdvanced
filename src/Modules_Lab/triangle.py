def print_triangle(size):
    for row in range(1, size + 2):
        print(*[i for i in range(1, row)])
    for row in range(size, 0, -1):
        print(*[i for i in range(1, row)])
