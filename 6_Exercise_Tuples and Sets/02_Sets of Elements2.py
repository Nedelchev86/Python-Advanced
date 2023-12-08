# first_set, second_set = set(), set()
# first, second = [int(x) for x in input().split()]
#
# for _ in range(first):
#     first_set.add(int(input()))
#
# for _ in range(second):
#     second_set.add(int(input()))
#
# print(*first_set.intersection(second_set), sep="\n")




first, second = [int(x) for x in input().split()]

first_set = {int(input()) for _ in range(first)}
second_set = {int(input()) for _ in range(second)}

print(*first_set.intersection(second_set), sep="\n")
