'''numbers = list(map(float, input().split()))

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = 1
    else:
        occurrences[num] += 1

for number, times in occurrences.items():
    print(f"{number} - {times} times")
'''

numbers = tuple(float(n) for n in input().split())
s = set()

for number in numbers:
    if number not in s:
        s.add(number)
        print(f"{number} - {numbers.count(number)} times")
