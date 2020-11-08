import os

while True:
    line = input()
    if line == "End":
        break
    else:
        split_line = line.split("-")
        command = split_line[0]

        if command == "Create":
            file_name = split_line[1]
            file = open(file_name, 'w')
            file.close()

        elif command == "Add":
            file_name = split_line[1]
            content = split_line[2]
            with open(file_name, 'a') as file:
                file.write(content + '\n')

        elif command == "Replace":
            file_name = split_line[1]
            old_string = split_line[2]
            new_string = split_line[3]
            try:
                with open(file_name, 'r') as in_file:
                    file_data = in_file.read()
                new_data = file_data.replace(old_string, new_string)
                with open(file_name, 'w') as out_file:
                    out_file.write(new_data)
            except:
                print("An error occurred")

        elif command == "Delete":
            file_name = split_line[1]
            if os.path.exists(file_name):
                os.remove(file_name)
            else:
                print("An error occurred")
