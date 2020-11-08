input_data = input().split(", ")
n = int(input())

categories = {category: {} for category in input_data}

for _ in range(n):
    item = input().split(" - ")
    category = item[0]
    item_name = item[1]
    item_ques = item[2].split(";")
    item_quantity = int(item_ques[0].split(":")[1])
    item_quality = int(item_ques[1].split(":")[1])

    categories[category][item_name] = [item_quantity, item_quality]

total_quantities = 0
total_qualities = 0
for category, items in categories.items():
    for ques in items.values():
        total_quantities += ques[0]
        total_qualities += ques[1]

print(f"Count of items: {total_quantities}")
print(f"Average quality: {total_qualities/len(categories):.2f}")
for category, items in categories.items():
    print(f"{category} -> {', '.join([key for key in items])}")

'''
count_items = sum([sum([x[0] for x in list(categories[category].values())]) for category in categories])
average_quality = sum([sum([x[1] for x in list(categories[category].values())]) for category in categories]) / len(categories)
'''