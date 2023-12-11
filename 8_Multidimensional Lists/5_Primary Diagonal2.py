# n = int(input())
# matrix = []
# total = 0
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# for i in range(n):
#     total += matrix[i][i]
# print(total)


total = 0

matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

for i in range(len(matrix)):
    total += matrix[i][i]
print(total)