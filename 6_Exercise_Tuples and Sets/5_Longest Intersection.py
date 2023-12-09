def generate_seq(range_info):
    start, end = [int(x) for x in range_info.split(",")]
    return set(range(start, end + 1))


nums = int(input())
best_intersection = set()

for num in range(nums):
    data = input().split("-")

    first_set = generate_seq(data[0])
    second_set = generate_seq(data[1])
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in best_intersection)}] with length {len(best_intersection)}")


