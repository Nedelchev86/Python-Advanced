from collections import deque

number = int(input())
my_stack = deque()

for i in range(number):
    data = input().split()
    command = data[0]
    if command == "1":
        my_stack.append(int(data[1]))
    elif command == "2" and my_stack:
        my_stack.pop()
    elif command == "3" and my_stack:
        print(max(my_stack))
    elif command == "4" and my_stack:
        print(min(my_stack))
while my_stack:
    element = my_stack.pop()
    if my_stack:
        print(element, end=", ")
    else:
        print(element)


#
# number = int(input())
# my_stack = []
#
# for i in range(number):
#     data = input().split()
#     command = data[0]
#     if command == "1":
#         my_stack.append(int(data[1]))
#     elif command == "2" and my_stack:
#         my_stack.pop()
#     elif command == "3" and my_stack:
#         print(max(my_stack))
#     elif command == "4" and my_stack:
#         print(min(my_stack))
# while my_stack:
#     element = my_stack.pop()
#     if my_stack:
#         print(element, end=", ")
#     else:
#         print(element)
