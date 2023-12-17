size = int(input())
car_number = input()

car = [0, 0]

race = []
tunnel = []
km = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    race.append(input().split())
    if "T" in race[row]:
        tunnel.append((row, race[row].index("T")))

while True:
    command = input()
    if command == "End":
        race[car[0]][car[1]] = "C"
        print(f"Racing car {car_number} DNF.")
        break

    n_row, n_col = car[0] + directions[command][0], car[1] + directions[command][1]

    next_position = race[n_row][n_col]

    if next_position == "F":
        km += 10
        race[n_row][n_col] = "C"
        print(f"Racing car {car_number} finished the stage!")
        break
    elif next_position == "T":
        km += 30
        race[n_row][n_col] = "."
        if n_row == tunnel[0][0] and n_col == tunnel[0][1]:
            car = [tunnel[1][0], tunnel[1][1]]
        else:
            car = [tunnel[0][0], tunnel[0][1]]
        race[car[0]][car[1]] = "."
    else:
        km += 10
        car = [n_row, n_col]

print(f"Distance covered {km} km.")
[print(*row, sep="") for row in race]
