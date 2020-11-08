def list_manipulator(numbers, action, position, *nums):
    result_list = []

    if action == "add":
        if len(nums) > 0:
            if position == "beginning":
                result_list = [x for x in list(nums)] + numbers
            elif position == "end":
                result_list = numbers + [x for x in list(nums)]

    elif action == "remove":
        if 0 <= len(nums) <= 1:
            n = nums[0] if len(nums) == 1 else 1
            if position == "beginning":
                result_list = [numbers[i] for i in range(n, len(numbers))]
            elif position == "end":
                result_list = [numbers[i] for i in range(len(numbers) - n)]

    return result_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

