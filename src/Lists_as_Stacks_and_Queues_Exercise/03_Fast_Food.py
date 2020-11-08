from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(i) for i in orders])}")
