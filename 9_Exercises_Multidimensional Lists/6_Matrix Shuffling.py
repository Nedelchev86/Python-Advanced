# rows , cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for row in range(rows):
#     matrix.append(input().split())
#
# while True:
#     data = input().split()
#     command = data[0]
#     if command == "END":
#         break
#     elif command == "swap" and len(data) == 5:
#         if int(data[1])  >= 0 and  int(data[1]) < rows  and int(data[2]) >= 0 and  int(data[2]) < cols and int(data[3])  >= 0 and  int(data[3]) < rows and  int(data[4]) >= 0 and int(data[4]) < cols:
#             matrix[int(data[1])][int(data[2])], matrix[int(data[3])][int(data[4])] = matrix[int(data[3])][int(data[4])], matrix[int(data[1])][int(data[2])]
#             for i in matrix:
#                 print(" ".join(i))
#         else:
#             print("Invalid input!")
#     else:
#         print("Invalid input!")



rows , cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


while True:
    data = input()
    if data == "END":
        break
    command_arge = data.split()

    if len(command_arge) != 5 or command_arge[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command_arge[1:]]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print("Invalid input!")
        continue
    else:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            # print(*row)
            print(*row, sep=" ")

