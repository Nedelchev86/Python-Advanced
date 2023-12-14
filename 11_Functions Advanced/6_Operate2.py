from functools import reduce

def operate(operator, *args):

    def opetaror_sum(*args):
        return reduce(lambda x, y: x + y, args)

    def opetaror_subtraction(*args):
        return reduce(lambda x, y: x - y, args)

    def opetaror_multiplication(*args):
        return reduce(lambda x, y: x * y, args)

    def opetaror_division(*args):
        return reduce(lambda x, y: x / y, args)

    if operator == "+":
        return opetaror_sum(*args)
    elif operator == "-":
        return opetaror_subtraction(*args)
    elif operator == "*":
        return opetaror_multiplication(*args)
    elif operator == "/":
        return opetaror_division(*args)


print(operate("+", 1, 2, 3))
print(operate("-", 3, 4))
