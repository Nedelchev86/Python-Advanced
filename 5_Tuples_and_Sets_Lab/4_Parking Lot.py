nums = int(input())
in_parking = set()

for i in range(nums):
    command, number = input().split(", ")
    if command == "IN":
        in_parking.add(number)
    else:
        in_parking.remove(number)
if in_parking:
    print("\n".join(in_parking))
else:
    print("Parking Lot is Empty")