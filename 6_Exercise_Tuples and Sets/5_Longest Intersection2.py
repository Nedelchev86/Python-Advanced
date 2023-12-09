def generate_seq(range_info):
    start, end = [int(x) for x in range_info.split(",")]
    return set(range(start, end + 1))

longest_intersection = set()

for _ in range(int(input())):
    first, second = input().split("-")
    first_set = generate_seq(first)
    second_set = generate_seq(second)
    current = first_set.intersection(second_set)
    if len(current) > len(longest_intersection):
        longest_intersection = current
print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")
