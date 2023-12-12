def is_valid(row, col):
    if row < rows and col < cols:
        return True
    return False

rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_valid(row1, col1) and is_valid(row2, col2):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for el in matrix:
            print(*el)
    else:
        print("Invalid input!")

