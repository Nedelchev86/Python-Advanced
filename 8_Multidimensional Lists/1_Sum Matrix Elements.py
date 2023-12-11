# rorw , cols = [int(x) for x in input().split(", ")]
# matrix = []
# total = 0
#
# for row in range(rorw):
#     current_input = [int(x) for x in input().split(", ")]
#     matrix.append(current_input)
#     total += sum(current_input)
#
# print(total)
# print(matrix)


# rorw , cols = [int(x) for x in input().split(", ")]
# matrix = []
# result = 0
#
# for row in range(rorw):
#     nums = [int(el) for el in input().split(", ")]
#     result += sum(nums)
#     matrix.append(nums)
#
# print(result)
# print(matrix)



# rorw , cols = [int(x) for x in input().split(", ")]
# matrix = []
# result = 0
#
# for row in range(rorw):
#     nums = [int(el) for el in input().split(", ")]
#     matrix.append(nums)
# for i in matrix:
#     result += sum(i)
#
# print(result)
# print(matrix)


rorw , cols = [int(x) for x in input().split(", ")]
matrix = []
result = 0

for row in range(rorw):
    nums = [int(el) for el in input().split(", ")]
    matrix.append(nums)
for row_ind in range(len(matrix)):
    for col in range(len(matrix[row])):
        result += matrix[row_ind][col]

print(result)
print(matrix)