n = int(input())

guests = set()
vips = set()

for _ in range(n):
    guest = input()
    guests.add(guest)

while True:
    token = input()
    if token == "END":
        break
    else:
        guests.remove(token)

print(len(guests))

for g in sorted(guests):
    print(g)