from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_toys = {}

while materials and magic_values:
    current_material = materials.pop()
    current_magic = magic_values.popleft()
    current_product = current_material * current_magic

    if current_product in presents:
        new_key = presents[current_product]
        if new_key not in crafted_toys:
            crafted_toys[new_key] = 1
        else:
            crafted_toys[new_key] += 1
        continue

    if current_product < 0:
        materials.append(current_material + current_magic)
    elif current_product > 0:
        materials.append(current_material + 15)
    else:
        if current_material != 0:
            materials.append(current_material)

        if current_magic != 0:
            magic_values.appendleft(current_magic)


if ("Dolls" in crafted_toys and "Wooden train" in crafted_toys)\
        or ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
elif magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for toy, amount in sorted(crafted_toys.items()):
    print(f"{toy}: {amount}")

