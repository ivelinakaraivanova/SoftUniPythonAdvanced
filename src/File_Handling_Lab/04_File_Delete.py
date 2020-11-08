import os

try:
    os.remove('D:/Iva/Python Advanced/Materials/Exercises/08-File-Handling-Lab-Resources/my_first_file.txt')
except FileNotFoundError:
    print("File already deleted!")
