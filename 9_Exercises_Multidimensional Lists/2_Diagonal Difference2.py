matrix = [[int(x) for x in input().split(' ')] for _ in range(int(input()))]

primary, secondary = list(), list()

for row in range(len(matrix)):
    start_row = len(matrix) - 1
    primary.append(matrix[row][row])
    secondary.append(matrix[row][start_row - row])

print(abs(sum(primary) - sum(secondary)))