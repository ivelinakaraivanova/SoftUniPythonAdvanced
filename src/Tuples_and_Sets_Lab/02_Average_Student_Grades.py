def average(some_list):
    return sum(some_list) / len(some_list)


n = int(input())

students = {}

for i in range(n):
    info = input().split()
    name = info[0]
    grade = float(info[1])
    if name not in students:
        students[name] = []
    students[name] += [grade]

for student, grades in students.items():
    print(f"{student} -> {' '.join(map(lambda f: format(f, '.2f'), grades))} (avg: {average(grades):.2f})")

