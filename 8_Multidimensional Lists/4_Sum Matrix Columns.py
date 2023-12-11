# rows, cols = list(map(int, input().split(", ")))
# matrix = []
# total = 0
#
# for row in range(rows):
#     matrix.append(list(map(int, input().split())))
#
# for i in range(cols):
#     print(sum([col[i] for col in matrix]))




# rows, cols = list(map(int, input().split(", ")))
# matrix = []
# total = 0
#
# for row in range(rows):
#     matrix.append([int(el) for el in input().split()])
#
# for col in range(cols):
#     total = 0
#     for row in range(rows):
#         total += matrix[row][col]
#     print(total)



# rows, cols = list(map(int, input().split(", ")))
# matrix = []
#
# for row in range(rows):
#     matrix.append([int(el) for el in input().split()])
#
# for col in range(cols):
#     result = 0
#     for row in range(rows):
#         result += matrix[row][col]
#     print(result)


rows, cols = list(map(int, input().split(", ")))
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for col in range(cols):
    print(sum([x[col] for x in matrix]))

