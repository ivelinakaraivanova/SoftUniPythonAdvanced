n = int(input())

usernames = set()

for _ in range(n):
    name = input()
    usernames.add(name)

print("\n".join(usernames))