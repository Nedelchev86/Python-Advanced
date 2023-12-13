
n = int(input())
matrix = []

for row in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    commaand = input().split()
    if commaand[0] == "END":
        break

    row, col, value = [int(x) for x in commaand[1:]]

    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid coordinates")
        continue
    if commaand[0] == "Add":
            matrix[row][col] += value
    elif commaand[0] == "Subtract":
            matrix[row][col] -= value
for row in matrix:
    print(*row)