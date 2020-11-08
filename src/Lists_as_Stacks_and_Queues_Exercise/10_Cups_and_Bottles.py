from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))

wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    capacity_difference = current_cup - current_bottle

    if capacity_difference > 0:
        current_cup -= current_bottle
        while True:
            next_bottle = bottles.pop()
            next_difference = current_cup - next_bottle
            if next_difference > 0:
                current_cup -= next_bottle
            else:
                wasted_water -= next_difference
                break

    else:
        wasted_water -= capacity_difference

if bottles:
    print(f"Bottles: {' '.join([str(b) for b in bottles])}")

elif cups:
    print(f"Cups: {' '.join([str(c) for c in cups])}")

print(f"Wasted litters of water: {wasted_water}")