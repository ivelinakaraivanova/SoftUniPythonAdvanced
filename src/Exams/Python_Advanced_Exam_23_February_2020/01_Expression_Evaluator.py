from collections import deque


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


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


expression = deque([x for x in input().split()])

temp_deq = deque()

while len(expression) > 1:
        element = expression.popleft()
        while is_number(element):
            temp_deq.append(element)
            element = expression.popleft()
        operator = element
        new_element = operate(operator, *[int(x) for x in temp_deq])
        expression.appendleft(str(int(new_element)))
        temp_deq = deque()

result = "".join(x for x in expression)
print(int(float(result)))
