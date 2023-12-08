# nums = int(input())
# regular = set()
# vip = set()
# arrive = set()
#
#
# for i in range(nums):
#     guest = input()
#     if guest[0].isdigit():
#         vip.add(guest)
#     else:
#         regular.add(guest)
#
# while True:
#     missing_guest = input()
#     if missing_guest == "END":
#         break
#     arrive.add(missing_guest)
#
# sorted_vip = vip.difference(arrive)
# sorted_regular = regular.difference(arrive)
#
# print(len(sorted_vip)+len(sorted_regular))
# print("\n".join(sorted(sorted_vip)))
# print("\n".join(sorted(sorted_regular)))


nums = int(input())
guest = set()
arrive = set()

for i in range(nums):
    guest.add(input())

while True:
    arrive_gurst = input()
    if arrive_gurst == "END":
        break
    arrive.add(arrive_gurst)

missing_gust = guest.difference(arrive)
print(len(missing_gust))

for x in sorted(missing_gust):
    print(x)