import math
from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()

    result = material + magic

    if result < 100:
        if result % 2 == 0:
            result = (2 * material) + (3 * magic)
        else:
            result += result
    if result < 100:
        continue

    if result > 499:
        result /= 2

    if 100 <= result <= 199:
        gifts["Gemstone"] += 1
    elif result <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif result <= 399:
        gifts["Gold"] += 1
    elif result <= 499:
        gifts["Diamond Jewellery"] += 1

if (gifts["Gemstone"] and gifts["Porcelain Sculpture"]) or (gifts["Gold"] and gifts["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f'Materials left: {", ".join(str(x) for x in materials)}')
if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')

for key, value in sorted(gifts.items(), key=lambda x: x[0]):
    if value:
        print(F"{key}: {value}")

