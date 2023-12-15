from collections import deque

time_sequence = deque(int(x) for x in input().split())
tasks_sequence = [int(x) for x in input().split()]

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
    }

while time_sequence or tasks_sequence:
    time = time_sequence.popleft()
    tasks = tasks_sequence.pop()
    result = time * tasks

    if 0 <= result <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        ducks["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        tasks -= 2
        tasks_sequence.append(tasks)
        time_sequence.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for key, value in ducks.items():
    print(f"{key}: {value}")
