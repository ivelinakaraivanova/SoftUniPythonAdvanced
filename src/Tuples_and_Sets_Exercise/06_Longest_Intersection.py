n = int(input())

intersections = []

for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = int(first_range.split(',')[0]), int(first_range.split(',')[1])
    second_start, second_end = int(second_range.split(',')[0]), int(second_range.split(',')[1])
    first_set = set()
    second_set = set()
    for i in range(first_start, first_end+1):
        first_set.add(i)
    for j in range(second_start, second_end+1):
        second_set.add(j)
    intersections.append(first_set & second_set)

max_intersec = max(intersections, key=len)
max_intersec_length = max(map(len, intersections))
max_intersec_list = [x for x in max_intersec]

print(f"Longest intersection is {max_intersec_list} with length {max_intersec_length}")


