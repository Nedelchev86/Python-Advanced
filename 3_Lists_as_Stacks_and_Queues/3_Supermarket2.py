# from collections import  deque
#
# queue = deque()
#
# while True:
#     command = input()
#     if command == "End":
#         print(F"{len(queue)} people remaining.")
#         break
#     elif command == "Paid":
#         while queue:
#             print(queue.popleft())
#     else:
#         queue.append(command)


from  collections import  deque

queue = deque()

while True:
    command = input()
    if command == "End":
        print(F"{len(queue)} people remaining.")
        break
    elif command == "Paid":
            print("\n".join(queue))
            queue.clear()
    else:
        queue.append(command)
