def validator(a, b, structure):
    return 0 <= a < rows and 0 <= b < cols


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)
while True:
    command, *data = input().split()

    if command == "END":
        break

    data_ints = [int(x) for x in data]
    if command == "swap" and len(data) == 4:
        if validator(data_ints[0], data_ints[1], matrix) and validator(data_ints[2], data_ints[3], matrix):
            matrix[data_ints[0]][data_ints[1]], matrix[data_ints[2]][data_ints[3]] = \
                matrix[data_ints[2]][data_ints[3]], matrix[data_ints[0]][data_ints[1]]

            print(*[' '.join(r) for r in matrix], sep="\n")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
