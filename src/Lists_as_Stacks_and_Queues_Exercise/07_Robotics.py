from collections import deque


def to_sec(time):
    h, m, s = list(map(int, time.split(":")))
    time_in_sec = h * 3600 + m * 60 + s
    return time_in_sec


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hour, minutes, seconds


robots_input = input().split(";")
start_time = to_sec(input())

available_robots = deque()
waiting_robots = deque()
robots_dict = {}
products = deque()

while True:
    product = input()
    if product == "End":
        break
    else:
        products.append(product)

for robot in robots_input:
    split_robot = robot.split("-")
    robot_name = split_robot[0]
    robot_time = int(split_robot[1])
    available_robots.append([robot_name, robot_time])
    robots_dict[robot_name] = robot_time

while products:
    for rob in waiting_robots:
        rob_name = rob[0]
        rob[1] -= 1
        if rob[1] <= 0:
            available_robots.append([rob_name, robots_dict[rob_name]])
    waiting_robots = [r for r in waiting_robots if r[1] > 0]

    start_time += 1
    hour, minn, sec = convert(start_time)
    current_product = products.popleft()

    if not available_robots:
        products.append(current_product)
        continue

    current_robot = available_robots.popleft()
    print(f"{current_robot[0]} - {current_product} [{hour:02d}:{minn:02d}:{sec:02d}]")
    waiting_robots.append(current_robot)

