from collections import deque

quantity = int(input())
people = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        people.append(name)

while True:
    command = input()
    if command == "End":
        break
    else:
        if "refill" in command:
            litters = int(command.split()[1])
            quantity += litters
        else:
            litters = int(command)
            if len(people) > 0:
                if litters <= quantity:
                    print(f"{people.popleft()} got water")
                    quantity -= litters
                else:
                    print(f"{people.popleft()} must wait")

print(f"{quantity} liters left")