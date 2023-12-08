# from collections import deque
#
# quantity = int(input())
# queue = deque([int(x) for x in input().split()])
# max = max(queue)
# while queue:
#     current_order = queue[0]
#     if quantity >= current_order:
#         quantity -= queue.popleft()
#     else:
#         break
# print(max)
# if queue:
#     print(F"Orders left: {' '.join([str(x) for x in queue])}")
# else:
#     print("Orders complete")
#

from collections import deque

quantity = int(input())
queue = deque([int(x) for x in input().split()])
max = max(queue)

print(max)

while queue:
    current_order = queue[0]
    if quantity >= current_order:
        quantity -= queue.popleft()
    else:
        print(F"Orders left: {' '.join([str(x) for x in queue])}")
        break

if not queue:
    print("Orders complete")

