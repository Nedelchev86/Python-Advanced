# data = input().split("|")
# matrix = []
#
# for i in range(len(data)):
#     matrix.append([data[i].replace("  "," ").strip()])
#
# for j in range(len(matrix) -1, -1, -1):
#     print("".join(matrix[j]), end=" ")
#


# data = input().split("|")
# result = []
# while data:
#     current_data = data.pop().split()
#     for el in current_data:
#         result.append(el)
# print(*result)


data = input().split("|")
while data:
    current_data = data.pop().split()
    for el in current_data:
        print(el, end=" ")


data = input().split("|")
while data:
    current_data = data.pop().split()
    if current_data:
        print(" ".join(current_data), end=" ")

