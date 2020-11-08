from collections import deque

people = deque(input().split())
n = int(input())

while len(people) > 1:
    people.rotate(-n)
    looser = people.pop()
    print(f"Removed {looser}")

winner = people.pop()
print(f"Last is {winner}")