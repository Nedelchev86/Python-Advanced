from collections import deque

boxes = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
    }

crafted_present = {}

while boxes and magic_level:
    box = boxes.pop()
    magic = magic_level.popleft()
    result = box * magic

    if result in toys:
        toy = toys[result]
        if toy in crafted_present:
            crafted_present[toy] += 1
        else:
            crafted_present[toy] = 1

    else:
        if result < 0:
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

if "Doll" in crafted_present and "Wooden train" in crafted_present or\
        "Teddy bear" in crafted_present and "Bicycle" in crafted_present:

    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join(str(x) for x in reversed(boxes))}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")


for key, value in sorted(crafted_present.items()):
    if value > 0:
        print(F"{key}: {value}")
