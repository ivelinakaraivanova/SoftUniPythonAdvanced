from collections import deque


green_light_time = int(input())
free_window_time = int(input())

cars = deque()
is_crashed = False
cars_count = 0

while True:
    command = input()
    if command == "END":
        break
    if command == "green":
        green_timer = green_light_time
        if cars:
            cars_copy = cars.popleft()
            current_car = deque(cars_copy)
            while green_timer:
                if not current_car:
                    if cars:
                        cars_copy = cars.popleft()
                        current_car = deque(cars_copy)
                    else:
                        break
                current_car.popleft()
                green_timer -= 1
            if current_car:
                window_timer = free_window_time
                while window_timer and current_car:
                    current_car.popleft()
                    window_timer -= 1
            if current_car:
                is_crashed = True
                print("A crash happened!")
                print(f"{cars_copy} was hit at {current_car.popleft()}.")
                break
    else:
        cars.append(command)
        cars_count += 1

if not is_crashed:
    print("Everyone is safe.")
    print(f"{cars_count - len(cars)} total cars passed the crossroads.")
