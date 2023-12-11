rows, cols = list(map(int, input().split(", ")))
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for col in range(cols):
    print(sum([x[col] for x in matrix]))


rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
total = 0

for col in range(cols):
    total = 0
    for row in range(rows):
        total += matrix[row][col]
    print(total)
