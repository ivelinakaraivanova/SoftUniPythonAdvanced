numbers = [int(x) for x in input().split(', ')]

positives = [num for num in numbers if num >= 0]
negatives = [num for num in numbers if num < 0]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print('Positive: ' + ', '.join(str(x) for x in positives))
print('Negative: ' + ', '.join(str(x) for x in negatives))
print('Even: ' + ', '.join(str(x) for x in evens))
print('Odd: ' + ', '.join(str(x) for x in odds))
