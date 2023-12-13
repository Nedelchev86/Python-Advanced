all_presents = int(input())
size = int(input())
neighborhood = []
santa = []
good_kids = 0
good_kids_present = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    neighborhood.append(input().split())
    if "S" in neighborhood[row]:
        santa = [row, neighborhood[row].index("S")]
        neighborhood[santa[0]][santa[1]] = "-"
    good_kids += neighborhood[row].count("V")

while all_presents:
    command = input()
    if command == "Christmas morning":
        break
    n_row, n_col = santa[0] + directions[command][0], santa[1] + directions[command][1]

    if neighborhood[n_row][n_col] == "V":
        all_presents -= 1
        good_kids_present += 1
    elif neighborhood[n_row][n_col] == "C":
        santa = [n_row, n_col]
        for direction in directions:
            if all_presents and good_kids > good_kids_present:
                n_row, n_col = santa[0] + directions[direction][0], santa[1] + directions[direction][1]
                if neighborhood[n_row][n_col] == "V":
                    all_presents -= 1
                    good_kids_present += 1

                elif neighborhood[n_row][n_col] == "X":
                    all_presents -= 1
                neighborhood[n_row][n_col] = "-"
                n_row, n_col = santa[0], santa[1]
            else:
                break
    neighborhood[santa[0]][santa[1]] = "-"
    santa = [n_row, n_col]

neighborhood[n_row][n_col] = "S"

if not all_presents and good_kids > good_kids_present:
    print("Santa ran out of presents!")
[print(*matrix) for matrix in neighborhood]
if good_kids == good_kids_present:
    print(f"Good job, Santa! {good_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids - good_kids_present} nice kid/s.")


