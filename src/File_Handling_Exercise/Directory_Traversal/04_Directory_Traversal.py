import os

path = input()
separators_count = path.count(os.path.sep)
files_dict = {}

for root, dirs, files in os.walk(path):
    if (separators_count - root.count(os.path.sep)) > 1:
        continue
    for file in files:
        extension = file.split(".")[-1]
        if extension not in files_dict:
            files_dict[extension] = []
        files_dict[extension].append(file)

sorted_files = dict(sorted(files_dict.items()))
result_string = ""

for ext, files in sorted_files.items():
    result_string += f".{ext}\n"
    sorted_files_lists = sorted(files)
    for file in sorted_files_lists:
        result_string += f'- - - {file}\n'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
location = desktop + os.path.sep + 'report.txt'

with open(location, 'w') as file:
    file.write(result_string)
