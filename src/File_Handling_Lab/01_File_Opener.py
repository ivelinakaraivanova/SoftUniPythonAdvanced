file_path = 'D:/Iva/Python Advanced/Materials/Exercises/08-File-Handling-Lab-Resources/File Opener/text.txt'

try:
    open(file_path, 'r')
    print("File found")
except:
    print("File not found")
