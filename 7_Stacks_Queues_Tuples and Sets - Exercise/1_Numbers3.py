first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}

for _ in range(int(input())):
    command, sets, *args = input().split()

    if command == "Add":
        if sets == "First":
            [first_set.add(int(el)) for el in args]
        else:
            [second_set.add(int(el)) for el in args]
    elif command == "Remove":
        if sets == "First":
            [first_set.discard(int(el)) for el in args]
        else:
            [second_set.discard(int(el)) for el in args]
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
