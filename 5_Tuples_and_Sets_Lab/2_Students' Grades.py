num = int(input())

students = dict()

for i in range(num):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for key, value in students.items():
    print(f"{key} -> {' '.join([str(f'{x:.2F}') for x in value])} (avg: {sum(value)/len(value):.2F})")
