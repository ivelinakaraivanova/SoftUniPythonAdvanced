input_line = input().split(', ')
strings_lengths = {string: len(string) for string in input_line}

print(", ".join('{} -> {}'.format(k, v) for k, v in strings_lengths.items()))
