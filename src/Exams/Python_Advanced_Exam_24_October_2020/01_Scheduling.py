jobs = [int(x) for x in input().split(", ")]
idx = int(input())

new_jobs = [(i, job) for i, job in enumerate(jobs)]

sorted_jobs = sorted(new_jobs, key=lambda x: x[1])

time_needed = 0

for item in sorted_jobs:
    time_needed += item[1]
    if item[0] == idx:
        break

print(time_needed)
