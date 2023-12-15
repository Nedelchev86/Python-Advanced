from collections import deque

seats = input().split(", ")
taken_seat = []
rotation = 0

first_sequence = deque(int(x) for x in input().split(", "))
second_sequence = deque(int(x) for x in input().split(", "))

while len(taken_seat) < 3 and rotation < 10:
    first = first_sequence.popleft()
    second = second_sequence.pop()
    rotation += 1

    result = chr(first + second)
    if f"{first}{result}" in seats:
        taken_seat.append(f"{first}{result}")
        seats.remove(f"{first}{result}")
    elif f"{second}{result}" in seats:
        taken_seat.append(f"{second}{result}")
        seats.remove(f"{second}{result}")
    else:
        first_sequence.append(first)
        second_sequence.appendleft(second)

print(f"Seat matches: {', '.join(taken_seat)}")
print(F"Rotations count: {rotation}")