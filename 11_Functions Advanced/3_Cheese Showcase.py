# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
#     result = ""
#     for name, quantity in sorted_cheeses:
#         result += name + "\n"
#         result += "\n".join([str(x) for x in sorted(quantity, reverse=True)]) + "\n"
#     return result


# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
#     result = ""
#     for name, quantity in sorted_cheeses:
#         result += name + "\n"
#         sorted_quantity = sorted(quantity, reverse=True)
#         result += "\n".join([str(x) for x in sorted_quantity]) + "\n"
#     return result


def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for name, quantity in sorted_cheeses:
        result += name + "\n"
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join(map(str, sorted_quantity)) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)