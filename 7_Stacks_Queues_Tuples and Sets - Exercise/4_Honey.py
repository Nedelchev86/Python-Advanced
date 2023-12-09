from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = deque(input().split())
result = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar >= bee:
        operation = symbols.popleft()
        if operation == "+":
            result += bee + nectar
        elif operation == "-":
            result += abs(bee - nectar)
        elif operation == "/" and nectar > 0:
            result += abs(bee / nectar)
        else:
            result += bee * nectar
    else:
        bees.appendleft(bee)


print(f"Total honey made: {result}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")
