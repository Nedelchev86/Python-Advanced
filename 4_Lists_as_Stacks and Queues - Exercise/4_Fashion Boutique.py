#
# clothes = list(map(int, input().split()))
# capacity = int(input())
# racks = 1
# current_rack = capacity
#
# while clothes:
#     if current_rack >= clothes[-1]:
#         current_rack -= clothes.pop()
#     else:
#         current_rack = capacity
#         racks += 1
# print(racks)
#
#


clothes = list(map(int, input().split()))
capacity = int(input())
racks = 1
current_rack = capacity

while clothes:
    current_clothes = clothes.pop()
    if current_rack >= current_clothes:
        current_rack -= current_clothes
    else:
        current_rack = capacity - current_clothes
        racks += 1
print(racks)


