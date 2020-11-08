# def find_strongest_eggs(sequence, number):
#     sub_lists = []
#     for _ in range(number):
#         sub_lists.append([])
#
#     for i in range(len(sub_lists)):
#         for s in range(i, len(sequence), number):
#             sub_lists[i].append(sequence[s])
#
#     strongest_eggs = []
#
#     def higher_than_neighbours(lst, item):
#         left_item = lst[lst.index(item)-1]
#         right_item = lst[lst.index(item)+1]
#         return item > left_item and item > right_item
#
#     def check_neighbours(lst, item):
#         return all(lst[lst.index(item)+idx+1] > lst[lst.index(item)-idx-1] for idx in range(len(lst)//2))
#
#     for sub_list in sub_lists:
#         middle_egg = sub_list[int(len(sub_list)/2)]
#         if higher_than_neighbours(sub_list, middle_egg) and check_neighbours(sub_list, middle_egg):
#             strongest_eggs.append(middle_egg)
#
#     return strongest_eggs


def find_strongest_eggs(eggs, number):
    strongest_eggs = []
    for i in range(number):
        current = [eggs[idx] for idx in range(i, len(eggs), number)]
        middle_egg = current[len(current) // 2]
        left_egg = current[len(current) // 2 - 1]
        right_egg = current[len(current) // 2 + 1]
        if left_egg < middle_egg > right_egg > left_egg:
            strongest_eggs.append(middle_egg)
    return strongest_eggs


# test = ([-1, 7, 3, 15, 2, 12], 2)
# print(find_strongest_eggs(*test))
#
# test = ([-1, 0, 2, 5, 2, 3], 2)
# print(find_strongest_eggs(*test))

test = ([58, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
