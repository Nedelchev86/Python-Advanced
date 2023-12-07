# from collections import deque
#
# def hot_potato(names, n):
#     queue = deque(names)
#     while len(queue) > 1:
#         for i in range(n-1):
#             queue.append(queue.popleft())
#         removed = queue.popleft()
#         print(f'Removed {removed}')
#     print(f'Last is {queue[0]}')
#
# names = input().split()
# n = int(input())
# hot_potato(names, n)


from collections import deque

names = input().split()
n = int(input())
queue = deque(names)

while len(queue) > 1:
    for i in range(n - 1):
        queue.append(queue.popleft())
    removed = queue.popleft()
    print(f'Removed {removed}')
print(f'Last is {queue[0]}')