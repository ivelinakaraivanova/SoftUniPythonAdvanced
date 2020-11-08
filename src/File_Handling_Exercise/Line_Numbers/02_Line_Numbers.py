import re

letters_pattern = r'\w'
marks_pattern = r'[\',.?!-;:\"]'
lines_and_counts = []

with open('text.txt', 'r') as input_file:
    row = 1
    for line in input_file.readlines():
        letters_count = len(re.findall(letters_pattern, line))
        marks_count = len(re.findall(marks_pattern, line))
        lines_and_counts.append((row, line, letters_count, marks_count))

        row += 1

with open('output.txt', 'w') as output_file:
    for item in lines_and_counts:
        row, line, letters_count, marks_count = item
        print(f'Line {row}: {line.rstrip()} ({letters_count})({marks_count})', file=output_file)


# with open('text.txt', 'r') as input_file:
#     row = 1
#     for line in input_file.readlines():
#         letters_count = len(re.findall(letters_pattern, line))
#         marks_count = len(re.findall(marks_pattern, line))
#         lines_and_counts.append((row, line, letters_count, marks_count))
#
#         with open('output.txt', 'a') as output_file:
#             output_file.write(f'Line {row}: {line[:-2]} ({letters_count})({marks_count})\n')
#         row += 1
