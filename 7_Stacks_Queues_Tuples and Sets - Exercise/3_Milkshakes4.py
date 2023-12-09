from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milk_cup = deque(int(x) for x in input().split(', '))

chocolate_milkshakes = 0

while chocolate_milkshakes < 5 and chocolates and milk_cup:
    choco = chocolates.pop()
    milk = milk_cup.popleft()

    if choco <= 0 and milk <= 0:
        continue

    elif choco <= 0:
        milk_cup.appendleft(milk)
        continue

    elif milk <= 0:
        chocolates.append(choco)
        continue

    if choco == milk:
        chocolate_milkshakes += 1
    else:
        milk_cup.append(milk)
        chocolates.append(choco - 5)

print("Great! You made all the chocolate milkshakes needed!") if chocolate_milkshakes == 5 else print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates)}") if chocolates else print("Chocolate: empty")
print(f"Milk: {', '.join(str(x) for x in milk_cup)}") if milk_cup else print("Milk: empty")
