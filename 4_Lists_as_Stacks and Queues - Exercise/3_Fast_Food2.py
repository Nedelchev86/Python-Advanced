from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    current_order = orders.popleft()
    if food >= current_order:
        food -= current_order
    else:
        orders.appendleft(current_order)
        break
if orders:
    # print(f"Orders left: {' '.join(str(x) for x in orders)}")
    print(f"Orders left:", *orders)
else:
    print("Orders complete")
