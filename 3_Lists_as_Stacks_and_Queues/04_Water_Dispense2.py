from collections import deque

quantity = int(input())
my_stack = deque()
name = input()

while not name == "Start":
    my_stack.append(name)
    name = input()

while True:
    command = input().split()
    if command[0] == "End":
        print(F"{quantity} liters left")
        break
    elif command[0] == "refill":
        quantity += int(command[1])
    else:
        litter = int(command[0])
        if quantity >= litter:
            print(f"{my_stack.popleft()} got water")
            quantity -= litter
        else:
            print(F"{my_stack.popleft()} must wait")
