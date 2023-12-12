rows, cols = [int(x) for x in input().split()]
ascii_start = 97
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(chr(ascii_start + row) + chr(ascii_start + row + col) + chr(ascii_start + row))
for i in matrix:
    print(" ".join(str(x) for x in i))