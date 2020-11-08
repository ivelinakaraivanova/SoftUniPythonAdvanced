n = int(input())

odds_set = set()
evens_set = set()

for i in range(1, n+1):
    name = input()
    name_sum = 0
    for c in name:
        name_sum += ord(c)
    name_value = name_sum // i

    if name_value % 2 == 0:
        evens_set.add(name_value)
    else:
        odds_set.add(name_value)

odd_sum = sum(odds_set)
even_sum = sum(evens_set)

if odd_sum == even_sum:
    print(', '.join([str(i) for i in (odds_set | evens_set)]))
elif odd_sum > even_sum:
    print(', '.join([str(i) for i in (odds_set - evens_set)]))
else:
    print(', '.join([str(i) for i in (odds_set ^ evens_set)]))