# from functools import reduce
#
# def fill_the_box(*args):
#     box_size = reduce(lambda x, y: x*y, args[:3])
#     cubes = 0
#     for i in range(3,len(args)-1):
#         if args[i] != "Finish":
#             cubes += args[i]
#         else:
#             break
#     if box_size - cubes > 0:
#         return F"There is free space in the box. You could put {box_size - cubes} more cubes."
#     else:
#         return  F"No more free space! You have {cubes - box_size} more cubes."



# def fill_the_box(height, length,width, *args):
#     box_size = height * length * width
#     cubes = 0
#     for el in args:
#         if el != "Finish":
#             cubes += el
#         else:
#             break
#     if box_size - cubes > 0:
#         return F"There is free space in the box. You could put {box_size - cubes} more cubes."
#     else:
#         return  F"No more free space! You have {cubes - box_size} more cubes."


def fill_the_box(height, length,width, *args):
    box_size = height * length * width
    cubes = 0
    left_cubes = 0
    for el in args:
        if el == "Finish":
            break
        if box_size >= el:
            box_size -= el
        else:
            el -= box_size
            left_cubes += el
            box_size = 0

    if box_size:
        return F"There is free space in the box. You could put {box_size} more cubes."
    else:
        return  F"No more free space! You have {left_cubes} more cubes."




print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
