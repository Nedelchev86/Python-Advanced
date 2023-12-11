# rows = int(input())
#
# matrix = []
#
# for i in range(rows):
#     matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
# print(matrix)


# rows = int(input())
# print(list([int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(rows)))

print([[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(int(input()))])
