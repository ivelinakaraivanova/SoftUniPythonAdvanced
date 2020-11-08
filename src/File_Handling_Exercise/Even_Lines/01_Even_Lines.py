symbols_for_replacement = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as input_file:
    row = 0
    for line in input_file.readlines():
        if row % 2 == 0:
            for s in symbols_for_replacement:
                line = line.replace(s, '@')
            words_in_line = line.split()
            reversed_line = reversed(words_in_line)
            print(' '.join(reversed_line))
        row += 1
