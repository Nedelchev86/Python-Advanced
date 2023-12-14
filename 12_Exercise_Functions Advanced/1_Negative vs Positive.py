# def negative_positive(numbers_list):
#     negative = []
#     possitive = []
#     for el in numbers_list:
#         if el > 0:
#             possitive.append(el)
#         else:
#             negative.append(el)
#     print(sum(negative))
#     print(sum(possitive))
#     if sum(possitive) > abs(sum(negative)):
#         return "The positives are stronger than the negatives"
#     else:
#         return "The negatives are stronger than the positives"
#
#
# print(negative_positive([int(x) for x in(input().split())]))




# def negative_positive(numbers_list):
#     possitive = [x for x in numbers_list if x > 0]
#     negative = [x for x in numbers_list if x < 0]
#     print(sum(negative))
#     print(sum(possitive))
#
#     if (sum(possitive)) > abs(sum(negative)):
#         return "The positives are stronger than the negatives"
#     else:
#         return "The negatives are stronger than the positives"
#
#
# print(negative_positive([int(x) for x in(input().split())]))



def negative_positive(numbers_list):
    possitive = sum([x for x in numbers_list if x > 0])
    negative = sum([x for x in numbers_list if x < 0])
    print(negative)
    print(possitive)

    if possitive > abs(negative):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


print(negative_positive([int(x) for x in(input().split())]))




# numbers_list = [int(x) for x in(input().split())]
#
# possitive = sum([x for x in numbers_list if x > 0])
# negative = sum([x for x in numbers_list if x < 0])
# print(negative)
# print(possitive)
#
# if possitive > abs(negative):
#     print("The positives are stronger than the negatives")
# else:
#     print("The negatives are stronger than the positives")


def negative_positive(*args):
    negative = 0
    possitive = 0
    for el in args:
        if el > 0:
            possitive += el
        else:
            negative += el
    return  negative, possitive


nums = [int(x) for x in(input().split())]
negative, possitive = negative_positive(*nums)

print(negative)
print(possitive)

if possitive > abs(negative):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")