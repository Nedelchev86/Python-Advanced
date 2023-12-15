matrix = []
size = int(input())
position = []

movement = input().split(', ')
hazelnuts = 0


def next_position(i, j, move):
    if move == "up":
        return i - 1, j
    elif move == "down":
        return i + 1, j
    elif move == "left":
        return i, j - 1
    elif move == "right":
        return i, j + 1


def is_valid_position(n_row, n_col, size):
    return 0 <= n_row < size and 0 <= n_col < size


for row in range(size):
    some_string = list(input())
    if "s" in some_string:
        position = [row, some_string.index("s")]
    matrix.append(some_string)

for move in movement:
    c_row, c_col = position
    n_row, n_col = next_position(c_row, c_col, move)
    if is_valid_position(n_row, n_col, size):
        c_row, c_col = n_row, n_col
        if matrix[c_row][c_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        elif matrix[c_row][c_col] == "h":
            matrix[c_row][c_col] = "s"
            hazelnuts += 1
            position = [c_row, c_col]
        else:
            position = [c_row, c_col]
            continue
    else:
        print("The squirrel is out of the field.")
        break
else:
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
    else:
        print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
