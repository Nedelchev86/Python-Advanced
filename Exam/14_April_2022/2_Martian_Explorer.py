matrix = []
rover = []


def next_position(row, col, direction):
    if direction == 'up':
         row = row - 1
    elif direction == 'down':
        row = row + 1
    elif direction == 'left':
         col = col - 1
    elif direction == 'right':
         col = col + 1
    return row, col


def check_valid_index(row, col):
    if row < 0:
        row = 5
    elif row > 5:
        row = 0
    if col < 0:
        col = 5
    elif col > 5:
        col = 0
    return row, col


deposits = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}

found = set()

for row in range(6):
    matrix.append(input().split())
    if "E" in matrix[row]:
        rover = [row, matrix[row].index("E")]

command_list = input().split(", ")

for command in command_list:
    n_row, n_col = next_position(rover[0], rover[1], command)
    n_row, n_col = check_valid_index(n_row, n_col)

    position = matrix[n_row][n_col]

    if position in "WMC":
        print(f"{deposits[position]} deposit found at ({n_row}, {n_col})")
        found.add(position)
    elif position == "R":
        print(F"Rover got broken at ({n_row}, {n_col})")
    rover = [n_row, n_col]

if len(found) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
