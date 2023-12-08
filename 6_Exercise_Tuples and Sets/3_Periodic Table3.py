unique_set = set()

for num in range(int(input())):
    for el in input().split():
        unique_set.add(el)
print("\n".join(unique_set))
