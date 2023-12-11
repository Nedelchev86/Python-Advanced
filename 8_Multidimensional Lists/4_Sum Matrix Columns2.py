# rows, cols = [int(x) for x in input().split(", ")]
#
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# total = 0
#
# for col in range(cols):
#     total = 0
#     for row in range(rows):
#         total += matrix[row][col]
#     print(total)


rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col in range(cols):
    print(sum(x[col] for x in matrix))
