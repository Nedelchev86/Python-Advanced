# n = int(input())
# matrix = []
#
# for row in range(n):
#     string = list(input())
#     matrix.append(string)
#
# symbol = input()
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         if symbol == matrix[row][col]:
#             print(F"({row}, {col})")
#             exit()
#
# print(F"{symbol} does not occur in the matrix")



# n = int(input())
# matrix = []
#
# for row in range(n):
#     string = list(input())
#     matrix.append(string)
#
# symbol = input()
# find = False
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         if symbol == matrix[row][col]:
#             print(F"({row}, {col})")
#             find = True
#     if find:
#         break
# if not find:
#     print(F"{symbol} does not occur in the matrix")





n = int(input())
matrix = []

for row in range(n):
    matrix.append(list(input()))

symbol = input()
position = []

for row in range(n):
    for col in range(n):
        if symbol == matrix[row][col]:
            position = (row, col)
            break
    if position:
        break

if position:
    print((position))
else:
    print(F"{symbol} does not occur in the matrix")
