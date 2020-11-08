import mathops

expression = input()
result = mathops.exec(*mathops.get_input(expression))
print(f'{result:.2f}')