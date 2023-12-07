data = input()
my_stack = []

for idx in range(len(data)):
    current = data[idx]
    if current == "(":
        my_stack.append(idx)
    elif current == ")":
        start_index = my_stack.pop()
        print(data[start_index:idx +1])