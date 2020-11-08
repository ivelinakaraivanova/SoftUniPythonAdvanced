import math

n = int(input())
base = input()

if base == "natural":
    result = math.log(n)
else:
    base = int(base)
    result = math.log(n, base)

print(f'{result:.2f}')
