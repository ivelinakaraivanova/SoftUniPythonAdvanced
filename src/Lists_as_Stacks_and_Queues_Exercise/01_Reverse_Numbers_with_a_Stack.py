numbers = input()
stack = []

for char in numbers:
    stack.append(char)

reversed_string = ''

while len(stack) > 0:
    item = stack.pop()
    reversed_string += item

print(reversed_string)