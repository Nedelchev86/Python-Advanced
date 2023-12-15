SIZE = 6

matrix = [input().split() for x in range(SIZE)]

c_row, c_col = [int(x) for x in input().strip("()").split(", ")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command == "Stop":
        break
    command, direction, *value = command.split(", ")

    n_row, n_col = c_row + directions[direction][0], c_col + directions[direction][1]
    next_position = matrix[n_row][n_col]

    if command == "Create":
        if next_position == ".":
            matrix[n_row][n_col] = value[0]
    elif command == "Update":
        if next_position != ".":
            matrix[n_row][n_col] = value[0]
    elif command == "Delete":
        matrix[n_row][n_col] = "."
    elif command == "Read":
        if next_position != ".":
            print(next_position)
    c_row, c_col = n_row, n_col


[print(*row) for row in matrix]