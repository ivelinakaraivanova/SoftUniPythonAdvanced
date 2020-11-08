n = int(input())

stack = []

for _ in range(n):
    command = input()
    if command.startswith('1'):
        element = int(command.split()[1])
        stack.append(element)
    else:
        if stack:
            if command == '2':
                stack.pop()
            elif command == '3':
                print(max(stack))
            elif command == "4":
                print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=', ')

if len(stack) == 1:
    print(stack.pop())