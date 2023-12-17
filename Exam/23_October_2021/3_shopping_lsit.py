def shopping_list(budget, **kwargs):
    my_basket = {}

    if budget < 100:
        return "You do not have enough budget."

    for product, (price, quantity) in kwargs.items():
        total = price * quantity
        if budget - total >= 0:
            my_basket[product] = total
            budget -= total
        if len(my_basket) == 5:
            break
    result = [f"You bought {key} for {value:.2F} leva." for key, value in my_basket.items()]
    return "\n".join(result)

