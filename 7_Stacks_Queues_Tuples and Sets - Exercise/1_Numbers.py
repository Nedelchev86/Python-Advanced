first_sequences = set([int(x) for x in input().split()])
second_sequences = set([int(x) for x in input().split()])

num = int(input())

for _ in range(num):
    data = input().split()
    command = data[0]
    sequence = data[1]

    if command == "Add":
        if sequence == "First":
            [first_sequences.add(int(x)) for x in data[2:]]
        else:
            [second_sequences.add(int(x)) for x in data[2:]]
    elif command == "Remove":
        current_set = data[2:]
        if sequence == "First":
            first_sequences = first_sequences.difference([int(x) for x in data[2:]])
        else:
            second_sequences = second_sequences.difference([int(x) for x in data[2:]])
    else:
        print(first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences))


print(*sorted(first_sequences), sep=", ")
print(*sorted(second_sequences), sep=", ")

