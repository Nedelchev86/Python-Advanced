# nums = int(input())
# unique_set = set()
#
# for i in range(nums):
#     name = input()
#     unique_set.add(name)
#
# print("\n".join(unique_set))


nums = int(input())
names = []

for i in range(nums):
    name = input()
    names.append(name)
unique_set = {name for name in names}

print("\n".join(unique_set))