# def get_repeating_DNA(string):
#     repeating_sequences = set()
#
#     def is_valid(some_string):
#         letters = ['A', 'C', 'G', 'T']
#         return all(c in letters for c in some_string)
#
#     if is_valid(string):
#         for s in range(len(string)-10):
#             searched_string = string[s:s+10]
#             for i in range(s+1, len(string)-9):
#                 new_string = string[i:i+10]
#                 if searched_string == new_string:
#                     repeating_sequences.add(searched_string)
#
#         return sorted(repeating_sequences)


# def get_repeating_DNA(string):
#
#     def is_valid(some_string):
#         letters = ['A', 'C', 'G', 'T']
#         return all(c in letters for c in some_string)
#
#     if is_valid(string):
#         strings = []
#         repeating_sequences = set()
#         for i in range(len(string)):
#             if i + 10 <= len(string):
#                 sub_string = string[i:i+10]
#                 strings.append(sub_string)
#
#         for s in strings:
#             count = strings.count(s)
#             if count >= 2:
#                 repeating_sequences.add(s)
#
#         return sorted(list(repeating_sequences))

from collections import defaultdict


def get_repeating_DNA(string):
    repeating_sequences = defaultdict(int)
    for i in range(len(string)-9):
        sub_string = string[i:i+10]
        repeating_sequences[sub_string] += 1

    sequences = [key for key, value in repeating_sequences.items() if value > 1]
    return sequences


test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)

