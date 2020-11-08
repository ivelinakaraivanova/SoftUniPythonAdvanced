n, m = list(map(int, input().split()))

set_n = set()
set_m = set()

for _ in range(n):
    number = int(input())
    set_n.add(number)

for _ in range(m):
    number = int(input())
    set_m.add(number)


intersec = set_n & set_m

print("\n".join([str(i) for i in intersec]))
