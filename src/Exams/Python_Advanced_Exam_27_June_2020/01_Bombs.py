from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

materials = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
    }

bombs_made = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}
is_fulfilled = False

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    current_bomb = current_effect + current_casing

    if current_bomb in materials:
        new_key = materials[current_bomb]
        bombs_made[new_key] += 1

        if all(x >= 3 for x in bombs_made.values()):
            is_fulfilled = True
            break

        continue

    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)


if is_fulfilled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for bomb, amount in sorted(bombs_made.items()):
    print(f"{bomb}: {amount}")
