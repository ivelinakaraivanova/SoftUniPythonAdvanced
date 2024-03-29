from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0
run_out_taxis = False

while customers:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

    if not taxis:
        run_out_taxis = True
        break

if len(customers) == 0:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    if run_out_taxis:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join([str(x) for x in customers])}")

