def fix_calendar(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


numbers = [8, 1, 0, 9, 25, 3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)

