rows, cols = [int(x) for x in input().split(', ')]
max_sum = -9999999
max_position = None

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col +1] + matrix[row + 1][col] + matrix[row + 1][col +1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_position = f"{matrix[row][col]} {matrix[row][col +1]}\n{matrix[row + 1][col]} {matrix[row +1][col +1]}"
print(max_position)
print(max_sum)
