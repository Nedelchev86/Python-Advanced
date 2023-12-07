# from collections import deque
#
# queue = deque()
#
# while True:
#     name = input()
#     if name == "End":
#         break
#     elif name == "Paid":
#         for i in range(len(queue)):
#             print(queue.popleft())
#     else:
#         queue.append(name)
# print(F"{len(queue)} people remaining.")


from collections import deque

queue = deque()

while True:
    name = input()
    if name == "End":
        break
    elif name == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)
print(F"{len(queue)} people remaining.")
