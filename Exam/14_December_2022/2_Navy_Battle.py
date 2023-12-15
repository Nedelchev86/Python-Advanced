battlefield = []
submarine = []
hits = 0
ships = 0

for row in range(int(input())):
    battlefield.append(list(input()))
    if "S" in battlefield[row]:
        submarine = [row, battlefield[row].index("S")]
        battlefield[row][submarine[1]] = "-"
    ships += battlefield[row].count("C")


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    n_row, n_col = submarine[0] + directions[command][0], submarine[1] + directions[command][1]

    next_position = battlefield[n_row][n_col]

    if next_position == "*":
        battlefield[n_row][n_col] = "-"
        hits += 1
    elif next_position == "C":
        battlefield[n_row][n_col] = "-"
        ships -=1
        if ships == 0:
            battlefield[n_row][n_col] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    if hits == 3:
        battlefield[n_row][n_col] = "S"
        print(F"Mission failed, U-9 disappeared! Last known coordinates [{n_row}, {n_col}]!")
        break
    submarine = [n_row, n_col]


[print(*row, sep="") for row in battlefield]
