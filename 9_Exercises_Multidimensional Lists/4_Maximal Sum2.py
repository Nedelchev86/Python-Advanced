rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = -999999


for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col +1] + matrix[row][col + 2] \
                      + matrix[row +1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] \
                      + matrix[row +2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if current_sum > max_sum:
            max_sum = current_sum
            best = f"{matrix[row][col]} {matrix[row][col +1]} {matrix[row][col + 2]}\n" \
                   f"{matrix[row +1][col]} {matrix[row + 1][col + 1]} {matrix[row + 1][col + 2]}\n" \
                   f"{matrix[row +2][col]} {matrix[row + 2][col + 1]} {matrix[row + 2][col + 2]}"
print(f"Sum = {max_sum}")
print(best)
