from collections import deque


def best_list_pureness(*args):
    numbers = args[0]
    k = int(args[1])
    new_numbers = deque(numbers)
    rotations = []
    for r in range(k+1):
        pureness = 0
        for idx, num in enumerate(new_numbers):
            product = num * idx
            pureness += product
        rotations.append((pureness, r))
        last = new_numbers.pop()
        new_numbers.appendleft(last)

    sorted_rotations = sorted(rotations, key=lambda x: (x[0], -x[1]))
    highest_pureness = sorted_rotations[-1]
    return f"Best pureness {highest_pureness[0]} after {highest_pureness[1]} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
