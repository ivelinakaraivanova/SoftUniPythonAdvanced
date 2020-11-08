def even_odd(*args):
    numbers = [int(x) for x in args[:-1]]
    command = args[-1]
    even_numbers = [x for x in numbers if x % 2 == 0]
    odd_numbers = [x for x in numbers if x % 2 != 0]
    if command == "even":
        return even_numbers
    elif command == "odd":
        return odd_numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
