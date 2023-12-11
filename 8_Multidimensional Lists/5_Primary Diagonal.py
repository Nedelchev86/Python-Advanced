# n = int(input())
# matrix = []
# inx = 0
# for row in range(n):
#     matrix.append([int(el) for el in input().split()])
#
# for i in range(n):
#     total = 0
#     for j in range(n):
#         total += matrix[j][j]
# print(total)



# n = int(input())
# matrix = []
# total = 0
# for row in range(n):
#     matrix.append([int(el) for el in input().split()])
#
# for row in range(n):
#     for col in range(n):
#         if row == col:
#             total += matrix[row][col]
# print(total)


n = int(input())
matrix = []
diagonal = 0
for row in range(n):
    matrix.append([int(el) for el in input().split()])

for index in range(n):
    diagonal += matrix[index][index]
print(diagonal)
