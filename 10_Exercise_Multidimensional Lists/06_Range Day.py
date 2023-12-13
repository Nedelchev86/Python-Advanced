matrix = []

all_targets = 0
my_position = []
shoot_targets = 0
hit_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(5):
    matrix.append(input().split())
    all_targets += matrix[row].count("x")
    if "A" in matrix[row]:
        my_position = [row, matrix[row].index("A")]

for _ in range(int(input())):
    command, direction, *steps = input().split()

    if command == "move":
        step = int(steps[0])

        n_row, n_col = my_position[0] + directions[direction][0] * step, my_position[1] + directions[direction][1] * step
        if not (0 <= n_row < 5 and 0 <= n_col < 5):
            continue
        if matrix[n_row][n_col] != "x":
            my_position = [n_row, n_col]
    elif command == "shoot":
        n_row, n_col = my_position[0] + directions[direction][0], my_position[1] + directions[direction][1]
        for i in range(5):
            if not (0 <= n_row < 5 and 0 <= n_col < 5):
                break
            if matrix[n_row][n_col] == "x":
                shoot_targets += 1
                hit_position.append([n_row, n_col])
                matrix[n_row][n_col] = "."
                break
            n_row += directions[direction][0]
            n_col += directions[direction][1]
        if shoot_targets == all_targets:
            print(f'Training completed! All {all_targets} targets hit.')
            break

if shoot_targets < all_targets:
    print(f"Training not completed! {all_targets - shoot_targets} targets left.")
if hit_position:
    print(*hit_position, sep="\n")

