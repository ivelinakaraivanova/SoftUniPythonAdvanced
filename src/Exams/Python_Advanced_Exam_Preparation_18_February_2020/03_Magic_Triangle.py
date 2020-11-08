# def get_magic_triangle(n):
#     if n == 1:
#         return [[1]]
#     else:
#         row = [1]
#         result = get_magic_triangle(n-1)
#         new_row = result[-1]
#         for i in range(len(new_row)-1):
#             row.append(new_row[i] + new_row[i+1])
#         row += [1]
#         result.append(row)
#     return result
#
# print(get_magic_triangle(5))


# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     for row in range(2, n):
#         new_row = []
#         for col in range(row+1):
#             if col == 0 or col == row:
#                 new_row.append(1)
#             else:
#                 upper_left = triangle[row - 1][col - 1]
#                 upper_right = triangle[row - 1][col]
#                 new_value = upper_left + upper_right
#                 new_row.append(new_value)
#         triangle.append(new_row)
#     return triangle
#
#
# print(get_magic_triangle(5))


def get_magic_triangle(n):
    triangle = [[1] * row for row in range(1, n+1)]
    for row in range(2, n):
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    return triangle


print(get_magic_triangle(5))
