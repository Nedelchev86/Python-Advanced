# row, col = [int(x) for x in input().split(', ')]
# matrix = []
# result = 0
#
# for i in range(row):
#     matrix.append([int(x) for x in input().split(', ')])
#     result += sum(matrix[i])
# print(result)
# print(matrix)


row, col = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(", ")] for i in range(row)]
print(sum(sum(x) for x in matrix))
print(matrix)
