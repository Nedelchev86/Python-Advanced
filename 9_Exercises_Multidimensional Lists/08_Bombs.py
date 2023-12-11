def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    size = len(matrix)
    neighbours = []

    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbours.append([row, col - 1])

    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbours.append([row, col + 1])

    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbours.append([row - 1, col])

    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbours.append([row - 1, col + 1])

    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbours.append([row - 1, col - 1])

    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbours.append([row + 1, col])

    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbours.append([row + 1, col - 1])

    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbours.append([row + 1, col + 1])
    return neighbours


n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

for bomb in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb.split(",")]
    bomb_power = matrix[bomb_row][bomb_col]

    if bomb_power <= 0:
        continue
    matrix[bomb_row][bomb_col] = 0

    for row, col in get_neighbours(bomb_row, bomb_col, matrix):
        matrix[row][col] -= bomb_power
alive = 0
sum_alive = 0

for i in matrix:
    for j in i:
        if j > 0:
            alive += 1
            sum_alive += j
print(F"Alive cells: {alive}")
print(F"Sum: {sum_alive}")

for row in matrix:
    print(*row)
