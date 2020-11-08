'''
import itertools

numbers = [x for x in input().split(", ")]
n = len(numbers)
permutations = itertools.product('+-', repeat=n)

for permutation in permutations:
    zipped = list(zip(permutation, numbers))
    expression = "".join(itertools.chain(*zipped))
    nums = map(lambda z: int(z[1]) if z[0] == '+' else -int(z[1]), zipped)
    result = sum(nums)
    print(f"{expression}={result}")
'''


def expressions(numbers, current_result, expression=""):
    if not numbers:
        return[(expression, current_result)]
    result_plus = expressions(
        numbers[1:],
        current_result + numbers[0],
        f'{expression}+{numbers[0]}'
    )
    result_minus = expressions(
        numbers[1:],
        current_result - numbers[0],
        f'{expression}-{numbers[0]}'
    )
    return result_plus + result_minus


result = expressions([1] * 4, 0)
[print(f'{expr_str}={expr_res}') for (expr_str, expr_res) in result]
