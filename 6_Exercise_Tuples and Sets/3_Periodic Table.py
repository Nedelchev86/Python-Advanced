nums = int(input())
unique_set = set()

for num in range(nums):
    current_data = input().split()
    for i in current_data:
        unique_set.add(i)
print("\n".join(unique_set))

