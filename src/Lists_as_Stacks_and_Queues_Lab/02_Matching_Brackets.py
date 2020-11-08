input_string = input()
stack = []

for index, char in enumerate(input_string):
    if char == "(":
        stack.append(index)
    elif char == ")":
        end_index = index+1
        start_index = stack.pop()
        subexpression = input_string[start_index:end_index]
        print(subexpression)
