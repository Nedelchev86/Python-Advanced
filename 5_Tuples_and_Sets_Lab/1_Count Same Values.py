# numbers = [float(x) for x in input().split()]
# nums_dict = {}
#
# for nums in numbers:
#     if nums not in nums_dict:
#         nums_dict[nums] = 0
#     nums_dict[nums] += 1
#
# for key, value in nums_dict.items():
#     print(f"{key:.1F} - {value} times")


# numbers = (float(x) for x in input().split())
# nums_dict = {}
#
# for nums in numbers:
#     if nums not in nums_dict:
#         nums_dict[nums] = 0
#     nums_dict[nums] += 1
#
# for tuples in nums_dict.items():
#     print(f"{tuples[0]:.1F} - {tuples[1]} times")

numbers = tuple(float(x) for x in input().split())
unique = []

for nums in numbers:
    if nums not in unique:
        unique.append(nums)

for nums in unique:
    nums_count = numbers.count(nums)
    print(f"{nums} - {nums_count} times")
