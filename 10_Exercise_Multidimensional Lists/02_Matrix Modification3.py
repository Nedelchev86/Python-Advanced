
n = int(input())
matrix = []

for row in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    commaand = input().split()
    if commaand[0] == "END":
        break
    elif commaand[0] == "Add":
        row, col, value = [int(x) for x in commaand[1:]]
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif commaand[0] == "Subtract":
        row, col, value = [int(x) for x in commaand[1:]]
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
for row in matrix:
    print(*row)