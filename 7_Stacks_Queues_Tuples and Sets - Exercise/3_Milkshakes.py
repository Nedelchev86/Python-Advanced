from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milks = deque([int(x) for x in input().split(", ")])
shakes = 0

while True:
    if shakes == 5 or not chocolates or not milks:
        break
    chocolate = chocolates.pop()
    milk = milks.popleft()

    if milk <= 0 and chocolate <= 0:
        continue

    if chocolate <= 0:
        milks.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        shakes += 1
    else:
        milks.append(milk)
        chocolates.append(chocolate - 5)
if shakes == 5:
    print(F"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if milks:
    print(f"Milk: {', '.join(str(x) for x in milks)}")
else:
    print("Milk: empty")
