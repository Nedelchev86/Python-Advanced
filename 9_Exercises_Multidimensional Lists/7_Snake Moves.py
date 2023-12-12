#
# rows, cols = [int(x) for x in input().split()]
# word = input()
# idx = 0
# matrix = []
#
# for row in range(rows):
#     row_elements = []
#     for col in range(cols):
#         row_elements.append(word[idx % len(word)])
#         idx += 1
#     if row % 2 == 0:
#         print(*row_elements, sep="")
#     else:
#         print(*reversed(row_elements), sep="")



rows, cols = [int(x) for x in input().split()]
word = input()
idx = 0
matrix = []

for row in range(rows):
    row_elements = [None] * cols
    if row % 2 == 0:
        for col in range(cols):
            row_elements[col] = word[idx % len(word)]
            idx += 1
    else:
        for col in range(cols -1, -1, -1):
            row_elements[col] = word[idx % len(word)]
            idx += 1
    print(*row_elements, sep="")
