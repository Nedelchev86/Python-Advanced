def shop_from_grocery_list(budget, shopping_list, *args):
    for product, money in args:
        if product in shopping_list:
            if budget - money < 0:
                break
            budget -= money
            shopping_list.remove(product)
    if shopping_list:
        return f"You did not buy all the products. Missing products: {', '.join(shopping_list)}."
    else:
        return F"Shopping is successful. Remaining budget: {budget:.2F}."



print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))