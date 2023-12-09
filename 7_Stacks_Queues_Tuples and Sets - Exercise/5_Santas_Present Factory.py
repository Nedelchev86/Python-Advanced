from collections import deque

boxes = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
toys = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while boxes and magic_level:
    box = boxes.pop()
    magic = magic_level.popleft()
    result = box * magic

    if result == 150:
        toys["Doll"] += 1
    elif result == 250:
        toys["Wooden train"] += 1
    elif result == 300:
        toys["Teddy bear"] += 1
    elif result == 400:
        toys["Bicycle"] += 1

    elif result < 0:
        boxes.append(box + magic)
    elif result > 0:
        boxes.append(box + 15)
    else:
        if magic == 0 and box == 0:
            continue
        if box == 0:
            magic_level.appendleft(magic)
        if magic == 0:
            boxes.append(box)

if toys["Doll"] > 0 and toys["Wooden train"] or toys["Teddy bear"] > 0 and toys["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join(str(x) for x in reversed(boxes))}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

sorted_toys = dict(sorted(toys.items()))

for key, value in sorted_toys.items():
    if value > 0:
        print(F"{key}: {value}")
