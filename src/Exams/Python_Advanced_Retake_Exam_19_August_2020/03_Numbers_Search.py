def numbers_searching(*args):
    result_list = []

    unique_numbers = sorted(list(set(args)))
    missing_number = None
    for i in range(len(unique_numbers)-1):
        diff = unique_numbers[i + 1] - unique_numbers[i]
        if diff > 1:
            missing_number = unique_numbers[i] + 1
    result_list.append(missing_number)

    duplicates = []
    for n in args:
        if n not in duplicates:
            if args.count(n) > 1:
                duplicates.append(n)
    result_list.append(sorted(duplicates))

    return result_list


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
