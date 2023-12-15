rows, cols = [int(x) for x in input().split()]
fields = []

my_pos = []
touched = 0
moves = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    fields.append(input().split())
    if "B" in fields[row]:
        my_pos = [row, fields[row].index("B")]

while touched < 3:
    command = input()
    if command == "Finish":
        break

    n_row, n_col = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]

    if not 0 <= n_row < rows or not 0 <= n_col < cols:
        continue

    if fields[n_row][n_col] == "P":
        touched += 1
        fields[n_row][n_col] = "-"
    elif fields[n_row][n_col] == "O":
        continue
    moves += 1
    fields[n_row][n_col] = "-"
    my_pos = [n_row, n_col]

print(f"Game over!\nTouched opponents: {touched} Moves made: {moves}")


