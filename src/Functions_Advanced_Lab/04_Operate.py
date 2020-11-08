def operate(operator, *numbers):
    result = 0
    is_first = True
    for i in numbers:
        if is_first:
            result = i
            is_first = False
        else:
            if operator == "+":
                result += i
            elif operator == "-":
                result -= i
            elif operator == "*":
                result *= i
            elif operator == "/":
                result /= i

    return result


# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("/", 2))
print(operate("/", 2, 4, 1, 5, 3, 8))
