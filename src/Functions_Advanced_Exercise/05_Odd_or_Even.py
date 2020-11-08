command = input()
numbers = [int(x) for x in input().split()]
length = len(numbers)
odd_sum = sum([x for x in numbers if x % 2 != 0])
even_sum = sum([x for x in numbers if x % 2 == 0])

if command == "Odd":
    result = odd_sum
else:
    result = even_sum

print(result*length)

