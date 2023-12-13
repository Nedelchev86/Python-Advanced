def check_valid_indices(curr_row, curr_col):
    return 0 <= curr_row < SIZE and 0 <= curr_col < SIZE


SIZE = int(input())
matrix = []
bunny = []

best = 0
best_move = []
best_direction = ""

direction = {
    'left': (0, -1),
    'right': (0, 1),
    'down': (1, 0),
    'up': (-1, 0)
}

for row in range(SIZE):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny = [row, matrix[row].index("B")]

for move in direction:
    current_score = 0
    c_row, c_col = bunny[0], bunny[1]
    current_move = []
    while True:
        c_row, c_col = c_row + direction[move][0], c_col + direction[move][1]
        if not check_valid_indices(c_row, c_col) or matrix[c_row][c_col] == "X":
            break
        current_score += int(matrix[c_row][c_col])
        current_move.append([c_row, c_col])

    if current_score > best:
        best = current_score
        best_move = current_move
        best_direction = move

if best != 0:
    print(best_direction)
    print(*best_move, sep="\n")
    print(best)
