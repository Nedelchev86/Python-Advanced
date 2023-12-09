from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = []

while bees and nectar:
    bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= bee:
        symbol = symbols.popleft()
        if symbol == "+":
            honey.append(bee + current_nectar)
        elif symbol == "-":
            honey.append(abs(bee - current_nectar))
        elif symbol == "*":
            honey.append(bee * current_nectar)
        elif symbol == "/" and current_nectar > 0:
            honey.append(bee / current_nectar)

    else:
        bees.appendleft(bee)

print(f"Total honey made: {sum(honey)}")
if bees:
    print(F"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(F"Nectar left: {', '.join(str(x) for x in nectar)}")

    
