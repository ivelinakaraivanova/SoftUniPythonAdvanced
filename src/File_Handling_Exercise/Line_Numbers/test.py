with open('text.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            print('yes')
        else:
            print('no')