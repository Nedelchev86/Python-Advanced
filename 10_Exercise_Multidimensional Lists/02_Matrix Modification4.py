def is_valid(i, j, matrix_):
    return 0 <= i < len(matrix_) and 0 <= j < len(matrix_[i])


matrix = [[int(i) for i in input().split()] for x in range(int(input()))]

while True:
    command = input().split()
    if command[0] == "END":
        break
    row, col, value = [int(x) for x in command[1:]]
    if command[0] == "Add" and is_valid(row, col, matrix):
        matrix[row][col] += value
    elif command[0] == "Subtract" and is_valid(row, col, matrix):
        matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for el in matrix:
    print(*el)
