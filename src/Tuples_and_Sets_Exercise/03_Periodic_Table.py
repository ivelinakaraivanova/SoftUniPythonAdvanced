n = int(input())

elements = set()

for _ in range(n):
    line = [i for i in input().split()]
    for element in line:
        elements.add(element)

print('\n'.join(elements))
