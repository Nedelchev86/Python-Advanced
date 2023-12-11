from collections import deque

materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())

craft = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magics:
    material = materials.pop()
    magic = magics.popleft()

    current_value = material * magic

    if current_value in presents:
        craft[presents[current_value]] += 1
    elif current_value < 0:
        current_value = material + magic
        materials.append(current_value)
    elif current_value >0:
        material += 15
        materials.append(material)

    else:
        if magic == 0 and material == 0:
            continue
        if material == 0:
            magics.appendleft(magic)
        if magic == 0:
            materials.append(material)


if craft["Doll"] and craft["Wooden train"] or craft["Teddy bear"] and craft["Bicycle"]:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    reversed_materials = reversed(materials)
    print(f'Materials left: {", ".join(str(x) for x in reversed_materials)}')
if magics:
    print(f'Magic left: {", ".join(str(x) for x in magics)}')

for key, value in sorted(craft.items()):
    if value != 0:
        print(F"{key}: {value}")
