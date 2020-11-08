from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

barrel_counter = 0
is_out_of_locks = False
bullets_count = len(bullets)

for _ in range(len(bullets)):
    if locks:
        current_bullet = bullets.pop()
        current_lock = locks.popleft()

        if current_bullet <= current_lock:
            print("Bang!")
        else:
            print("Ping!")
            locks.appendleft(current_lock)
        barrel_counter += 1

        if barrel_counter == barrel_size and bullets:
            print("Reloading!")
            barrel_counter = 0

    else:
        is_out_of_locks = True
        break

bullets_left = len(bullets)
bullets_shot = bullets_count - bullets_left
money_earned = intelligence_value - bullets_shot * bullet_price

if is_out_of_locks or (len(locks) == 0 and len(bullets) == 0):
    print(f"{bullets_left} bullets left. Earned ${money_earned}")

else:
    locks_left = len(locks)
    print(f"Couldn't get through. Locks left: {locks_left}")
