first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}


for _ in range(int(input())):
    command, sets, *args = input().split()
    if command == "Add":
        if sets == "First":
            for el in args:
                first_set.add(int(el))
        else:
            for el in args:
                second_set.add(int(el))
    elif command == "Remove":
        current_set = set(int(x) for x in args)
        if sets == "First":
            first_set = first_set.difference(current_set)
        else:
            second_set = second_set.difference(current_set)
        # if sets == "First":
        #     for el in args:
        #         first_set.discard(el)
        # else:
        #     for el in args:
        #         second_set.discard(el)
    else:
        print(first_set.issuperset(second_set))
        # print(first_set.issubset(second_set) or second_set.issubset(first_set))

if first_set:
    print(*sorted(first_set), sep=", ")
if second_set:
    print(*sorted(second_set), sep=", ")
