sequence = input()

stack = []
is_valid = True

opening = ['(', '[', '{']
closing = [')', ']', '}']

for item in sequence:
    if item in opening:
        stack.append(item)
    elif item in closing:
        if len(stack) == 0:
            is_valid = False
        else:
            last_paren = stack.pop()
            if (last_paren == '(' and item == ')') or\
                    (last_paren == '[' and item == ']') or \
                    (last_paren == '{' and item == '}'):
                continue
            else:
                is_valid = False
                break

if is_valid:
    print("YES")
else:
    print("NO")
