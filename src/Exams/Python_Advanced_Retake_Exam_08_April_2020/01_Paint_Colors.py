def is_in_value(dictionary, some_string):
    return any(some_string in value for key, value in dictionary.items())


strings = input().split()

colors = {
    'main': ['red', 'yellow', 'blue'],
    'secondary': ['orange', 'purple', 'green']
}

sec_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

result_list = []

while strings:
    left_sub = strings.pop(0)

    if len(strings) > 0:
        right_sub = strings.pop()
    else:
        right_sub = ''

    new_string = left_sub + right_sub
    if is_in_value(colors, new_string):
        result_list.append(new_string)
    else:
        new_string = right_sub + left_sub
        if is_in_value(colors, new_string):
            result_list.append(new_string)
        else:
            left_sub = left_sub[:-1]
            right_sub = right_sub[:-1]
            mid_point = len(strings) // 2
            if len(left_sub) > 0:
                strings = strings[:mid_point] + [left_sub] + strings[mid_point:]
            if len(right_sub) > 0:
                strings = strings[:mid_point] + [right_sub] + strings[mid_point:]

for i in range(len(result_list)-1, -1, -1):
    if result_list[i] in sec_colors:
        if any(c not in result_list for c in sec_colors[result_list[i]]):
            result_list.remove(result_list[i])

print(result_list)
