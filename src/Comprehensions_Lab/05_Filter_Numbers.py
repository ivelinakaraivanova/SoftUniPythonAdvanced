start = int(input())
end = int(input())

result = [num for num in range(start, end+1) if any(num % x == 0 for x in range(2, 11))]

print(result)
