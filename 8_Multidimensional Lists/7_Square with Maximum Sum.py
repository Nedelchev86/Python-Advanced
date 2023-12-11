rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(",")])

max_sum = -888888
max_sum_matrix = []

for i in range(rows -1):
    for j in range(cols -1):
        sub_matrix = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = sub_matrix.copy()


print(max_sum_matrix[0], max_sum_matrix[1])
print(max_sum_matrix[2], max_sum_matrix[3])
print(max_sum)

