numbers = input().split()
stack = []

for item in numbers:
    stack.append(item)

reversed_numbers = ''
while len(stack) > 0:
    item = stack.pop()
    reversed_numbers += item + ' '

print(reversed_numbers)
