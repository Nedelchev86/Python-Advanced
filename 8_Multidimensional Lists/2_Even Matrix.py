# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
# print(matrix)


# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     data = list(map(int, input().split(", ")))
#     data = list(filter(lambda x: x % 2 == 0, data))
#
#     matrix.append(data)
# print(matrix)


#
# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     matrix.append(list(map(int, (filter(lambda x: int(x) % 2 == 0, input().split(", "))))))
# print(matrix)


# rows = int(input())
# matrix = []
# for _ in range(rows):
#     nums = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
#     matrix.append(nums)

# rows = int(input())
# matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(rows)]
# print(matrix)


print([[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))])