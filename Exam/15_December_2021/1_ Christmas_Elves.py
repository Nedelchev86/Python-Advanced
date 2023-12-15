from collections import deque

elf_energy = deque(int(x) for x in input().split())
materials_box = [int(x) for x in input().split()]
count = 0
toys = 0
spend_energy = 0

while elf_energy and materials_box:
    count += 1

    elf = elf_energy.popleft()
    material = materials_box.pop()

    if count % 3 == 0:
        if elf >= material*2:
            elf -= material
            elf_energy.append(elf + 1)
            toys += 2
            spend_energy += material
            continue
        else:
            elf_energy.append(elf + elf)

            materials_box.append(material)
            continue

    elif count % 5 == 0:
        spend_energy += material
        continue

    if elf >= material:

        elf -= material
        elf_energy.append(elf + 1)
        toys += 1
        spend_energy += material
    else:
        elf_energy.append(elf + elf)

        materials_box.append(material)

print(f"Toys: {toys}")
print(f"Energy: {spend_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if materials_box:
    print(f"Elves left: {', '.join(str(x) for x in materials_box)}")