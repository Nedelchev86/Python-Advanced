# rows, cols = [int(x) for x in input().split()]
# matrix = []
# max_sum = -99999999999
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
# max_size_list = []
#
# for row in range(rows-2):
#     for col in range(cols -2):
#         if matrix[row][col] + matrix[row][col+1] + matrix[row][col +2] + matrix[row +1][col] + matrix[row+1][col +1] + matrix[row+1][col +2] + matrix[row +2][col] + matrix[row+2][col +1] + matrix[row+2][col +2] > max_sum:
#             max_sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col +2] + matrix[row +1][col] + matrix[row+1][col +1] + matrix[row+1][col +2] + matrix[row +2][col] + matrix[row+2][col +1] + matrix[row+2][col +2]
#             max_size_list = [matrix[row][col], matrix[row][col+1], matrix[row][col +2], matrix[row +1][col], matrix[row+1][col +1], matrix[row+1][col +2], matrix[row +2][col], matrix[row+2][col +1], matrix[row+2][col +2]]
# print(F"Sum = {max_sum}")
# print(max_size_list[0], max_size_list[1], max_size_list[2])
# print(max_size_list[3], max_size_list[4], max_size_list[5])
# print(max_size_list[6], max_size_list[7], max_size_list[8])
#


rows, cols = [int(x) for x in input().split()]
matrix = []
max_sum = -99999999999

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

best_row = 0
best_col = 0

for row in range(rows-2):
    for col in range(cols -2):
        current_sum = matrix[row][col] + matrix[row][col+1] + matrix[row][col +2] +\
                      matrix[row +1][col] + matrix[row+1][col +1] + matrix[row+1][col +2] + \
                      matrix[row +2][col] + matrix[row+2][col +1] + matrix[row+2][col +2]

        if current_sum > max_sum:
            max_sum = current_sum
            best_row = row
            best_col = col

print(F"Sum = {max_sum}")
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col +2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col +2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col +2])

