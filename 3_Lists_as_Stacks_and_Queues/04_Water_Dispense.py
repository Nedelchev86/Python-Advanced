from collections import  deque

quantity_of_water = int(input())

people = deque()

while True:
    data = input()
    if data == "Start":
        break
    people.append(data)

while True:
    data = input()
    if data == "End":
        break
    data = data.split()
    if len(data) == 2:
        quantity_of_water += int(data[1])
    else:
        liters = int(data[0])
        person = people.popleft()
        if liters <= quantity_of_water:
            print(F"{person} got water")
            quantity_of_water -= liters
        else:
            print(F"{person} must wait")

print(F"{quantity_of_water} liters left")