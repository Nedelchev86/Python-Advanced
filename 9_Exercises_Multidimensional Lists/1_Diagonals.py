n = int(input())
matrix = []

for rows in range(n):
    matrix.append([int(x) for x in input().split(", ")])
left_diagonal = []
right_diagonal = []

for i in range(n):
    left_diagonal.append(matrix[i][i])
current = 0
for i in range(n -1, -1, -1):
    right_diagonal.append(matrix[current][i])
    current += 1

print(F"Primary diagonal: {', '.join([str(x) for x in left_diagonal])}. Sum: {sum(left_diagonal)}")
print(F"Secondary diagonal: {', '.join([str(x) for x in right_diagonal])}. Sum: {sum(right_diagonal)}")




# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split(", ")])
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for idx in range(size):
#     primary_diagonal.append(matrix[idx][idx])
#     secondary_diagonal.append((matrix[idx][size - 1 - idx]))
#
# print(F"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(F"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")





size = int(input())

primary_diagonal = []
secondary_diagonal = []

for idx in range(size):
    elements = ([int(x) for x in input().split(", ")])
    primary_diagonal.append(elements[idx])
    secondary_diagonal.append((elements[size - 1 - idx]))

print(F"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(F"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
