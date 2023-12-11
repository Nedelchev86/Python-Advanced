# rows, cols = [int(x) for x in input().split(", ")]

# for row in range(rows):
#     col = [int(x) for x in input().split(", ")]
#     matrix.append(col)
#
# print(sum([sum(x) for x in matrix]))
# print(matrix)

# rows, cols = [int(x) for x in input().split(", ")]
# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
# print(sum(sum(x) for x in matrix))
# print(matrix)


rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
print(sum(sum(x) for x in matrix))
print(matrix)
