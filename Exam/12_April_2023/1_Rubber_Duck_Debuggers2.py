from collections import deque


def found_duck(value):
    if 0 <= value <= 60:
        return "Darth Vader Ducky"
    elif 61 <= value <= 120:
        return "Thor Ducky"
    elif 121 <= value <= 180:
        return "Big Blue Rubber Ducky"
    elif 181 <= value <= 240:
        return "Small Yellow Rubber Ducky"


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

    if result > 240:
        tasks -= 2
        tasks_sequence.append(tasks)
        time_sequence.append(time)
    else:
        ducks[found_duck(result)] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for key, value in ducks.items():
    print(f"{key}: {value}")
