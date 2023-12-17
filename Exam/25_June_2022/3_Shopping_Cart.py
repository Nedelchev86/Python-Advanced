def shopping_cart(*args):
    my_dict = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }
    limit = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2,
    }
    for el in args:
        if el == "Stop":
            break
        meal, product = el[0], el[1]
        if product not in my_dict[meal] and not len(my_dict[meal]) == limit[meal]:
            my_dict[meal].append(product)
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []
    for meal, products in sorted_dict.items():
        result.append(f"{meal}:")
        for el in sorted(products):
            result.append(f" - {el}")
    if any(my_dict.values()):
        return "\n".join(result)
    return "No products in the cart!"

