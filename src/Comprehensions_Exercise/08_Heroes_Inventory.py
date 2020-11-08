names = input().split(", ")

inventory = {name: {} for name in names}

while True:
    info = input()
    if info == "End":
        break
    else:
        split_info = info.split("-")
        name = split_info[0]
        item = split_info[1]
        cost = int(split_info[2])
        if item not in inventory[name]:
            inventory[name][item] = cost

for name, items in inventory.items():
    items_cost = 0
    for cost in inventory[name].values():
        items_cost += cost
    print(f"{name} -> Items: {len(inventory[name])}, Cost: {items_cost}")


# [print(f"{name} -> Items: {len(inventory[name])}, Cost: {sum(inventory[name].values())}") for name in inventory]
