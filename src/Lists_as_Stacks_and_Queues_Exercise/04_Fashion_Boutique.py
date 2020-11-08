box = list(map(int, input().split()))
rack_capacity = int(input())

clothes = []
box_sum = 0
rack_count = 1

for item in box:
    clothes.append(item)

while clothes:
    box_sum += clothes[-1]
    if box_sum <= rack_capacity:
        clothes.pop()
    else:
        rack_count += 1
        box_sum = 0

print(rack_count)