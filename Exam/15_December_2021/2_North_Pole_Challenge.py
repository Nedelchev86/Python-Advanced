rows, cols = [int(x) for x in input().split(', ')]

matrix = []
santa = []
collect_all = False
def check_valid_index(row, col):
    if row < 0:
        row = rows - 1
    elif row >= rows:
        row = 0
    if col < 0:
        col =  cols - 1
    elif col >= cols:
        col = 0
    return row, col

items = {
    "D": "Christmas decorations",
    "G": "Gifts",
    "C": "Cookies",
}

must_find = {
    "D": 0,
    "G": 0,
    "C": 0,
}

collected = {
    "D": 0,
    "G": 0,
    "C": 0,
}

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


for row in range(rows):
    matrix.append(input().split())
    if "Y" in matrix[row]:
        santa = [row, matrix[row].index("Y")]
        matrix[santa[0]][santa[1]] = "x"
    must_find["D"] += matrix[row].count("D")
    must_find["G"] += matrix[row].count("G")
    must_find["C"] += matrix[row].count("C")

while True:
    command = input()

    if command == "End":
        matrix[santa[0]][santa[1]] = "Y"
        break
    direction, steps = [int(x) if x.isdigit() else x for x in command.split("-")]

    for _ in range(steps):
        n_row, n_col = santa[0] + directions[direction][0], santa[1] + directions[direction][1]
        n_row, n_col = check_valid_index(n_row, n_col)
        next_position = matrix[n_row][n_col]
        if next_position in "DGC":
            collected[next_position] += 1
        matrix[n_row][n_col] = "x"
        santa = [n_row, n_col]

        if collected["D"] == must_find["D"] and collected["C"] == must_find["C"] and collected["G"] == must_find["G"]:
            matrix[santa[0]][santa[1]] = "Y"
            print(F"Merry Christmas!")
            collect_all = True
            break
    if collect_all:
        break
print("You've collected:")
[print(F"- {value} {items[key]}") for key, value in collected.items()]

[print(*row) for row in matrix]
