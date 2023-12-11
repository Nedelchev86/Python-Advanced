matrix = [list(input()) for _ in range(int(input()))]

symbol = input()
find = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            find = True
        if find:
            break
if not find:
    print(F"{symbol} does not occur in the matrix")
