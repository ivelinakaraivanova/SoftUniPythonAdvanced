from collections import deque

names = deque()

while True:
    command = input()
    if command == "Paid":
        while len(names) > 0:
            print(names.popleft())
    elif command == "End":
        break
    else:
        name = command
        names.append(name)

print(f"{len(names)} people remaining.")