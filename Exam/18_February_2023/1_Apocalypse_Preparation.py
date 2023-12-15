from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

healing_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

maked_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    result = textile + medicament

    if result > 100:
        maked_items["MedKit"] += 1
        next_medicament = medicaments.pop() + (result - 100)
        medicaments.append(next_medicament)

    elif result in healing_items:
        maked_items[healing_items[result]] += 1

    else:
        medicaments.append(medicament+10)

if not textiles and medicaments:
    print("Textiles are empty.")
else:
    if not medicaments and textiles:
        print("Medicaments are empty.")
    if not medicaments and not textiles:
        print("Textiles and medicaments are both empty.")

for key, value in sorted(maked_items.items(), key=lambda i: (-i[1], i[0])):
    if value != 0:
        print(f"{key} - {value}")
if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in reversed(medicaments)])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
