# rows, cols = [int(x) for x in input().split()]
# matrix = []
# start = 97
# curent = 97
#
# for row in range(rows):
#     matrix.append([])
#
#     for col in range(cols):
#         matrix[row].append(chr(start)+chr(curent)+chr(start))
#         curent += 1
#     start +=1
#     curent = start
#
# for i in matrix:
#     print(" ".join(str(x) for x in i))




rows, cols = [int(x) for x in input().split()]
matrix = []
start = 97
current = 97

for row in range(rows):
    for col in range(cols):
        print(chr(start + row)+ chr(start + row + col)+ chr(start + row), end=" ")
    print()



rows, cols = [int(x) for x in input().split()]
matrix = []
start = 97

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(chr(start + row)+ chr(start + row + col)+ chr(start + row))

for i in matrix:
    print(" ".join(str(x) for x in i))
