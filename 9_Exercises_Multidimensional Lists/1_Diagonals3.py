# matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
# first_diagonal, second_diagonal = [], []
#
# for row in range(len(matrix)):
#     start_row = len(matrix) - 1
#     first_diagonal.append(matrix[row][row])
#     second_diagonal.append(matrix[row][start_row - row])
# print(f"Primary diagonal: {', '.join(str(x) for x in first_diagonal)}. Sum: {sum(first_diagonal)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {sum(second_diagonal)}")


n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n-1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
