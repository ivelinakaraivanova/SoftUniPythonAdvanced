def calculate_with_loop(file_path):
    file = open(file_path, 'r')
    result = 0

    for number_line in file:
        result += int(number_line)
    return result


def calculate_with_readline(file_path):
    file = open(file_path, 'r')
    result = 0

    while True:
        number_line = file.readline()
        if not number_line:
            break
        result += int(number_line)
    return result


file_path = 'D:/Iva/Python Advanced/Materials/Exercises/08-File-Handling-Lab-Resources/File Reader/numbers.txt'

print(calculate_with_loop(file_path))
print(calculate_with_readline(file_path))