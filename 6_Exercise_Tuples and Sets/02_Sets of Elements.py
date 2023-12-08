# line = (int(x) for x in input().split())
# first, second = line
#
# first_set = set()
# second_set = set()
#
# for num in range(first):
#     current_data = input()
#     first_set.add(current_data)
#
# for num in range(second):
#     current_data = input()
#     second_set.add(current_data)
#
# result = first_set.intersection(second_set)
# print("\n".join(result))


# first, second = (int(x) for x in input().split())
#
# first_set, second_set = set(), set()
#
# for num in range(first):
#     first_set.add(input())
#
# for num in range(second):
#     second_set.add(input())
#
# print("\n".join(first_set.intersection(second_set)))


first, second = (int(x) for x in input().split())

first_set, second_set = set(), set()

for num in range(first):
    first_set.add(input())

for num in range(second):
    second_set.add(input())

print("\n".join(first_set & second_set))
