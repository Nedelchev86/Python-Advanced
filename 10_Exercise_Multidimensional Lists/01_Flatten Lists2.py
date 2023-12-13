# some_list = input().replace("  ", " ").split("|")
#
# for el in range(len(some_list) -1, -1, -1):
#     print(some_list[el].strip(), end=" ")
#
#

#
#
# data = input().split("|")
# matrix = []
#
# for i in range(len(data)):
#     matrix.append([data[i].replace("  "," ").strip()])
#
# for j in range(len(matrix) -1, -1, -1):
#     print("".join(matrix[j]), end=" ")



# line = input().split("|")
#
# sublist = []
#
# for string in line[::-1]:
#     sublist.extend(string.split())
#
# print(*sublist)
#


# numbers = [string.split( ) for string in input().split("|")]
# print(*[" ".join(sublist) for sublist in numbers[::-1]])
