SIZE = int(input())

matrix = []
alice_position = []
tea = 0

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[alice_position[0]][alice_position[1]] = "*"


while tea < 10:
    move = input()
    n_row, n_col = alice_position[0] + direction[move][0], alice_position[1] + direction[move][1]

    if 0 <= n_col < SIZE and 0 <= n_row < SIZE:
        if matrix[n_row][n_col] == "R":
            matrix[n_row][n_col] = "*"
            break
        elif matrix[n_row][n_col].isdigit():
            tea += int(matrix[n_row][n_col])
        matrix[n_row][n_col] = "*"
        alice_position = [n_row, n_col]
    else:
        break

print("She did it! She went to the party.") if tea >= 10 else print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
