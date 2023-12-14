# def rectangle(num, num2):
#     if isinstance(num, int) and isinstance(num2, int):
#         return F"{area(num, num2)}\n{perimeter(num, num2)}"
#     else:
#         return "Enter valid values!"
#
#
#
# def area(num, num2):
#     return F"Rectangle area: {num * num2}"
#
#
# def perimeter(num, num2):
#     return F"Rectangle perimeter: {(num + num2)* 2}"
#
# print(rectangle(2, 10))
# print(rectangle('2', 10))


# def rectangle(num, num2):
#     def area(num, num2):
#         return F"Rectangle area: {num * num2}"
#
#     def perimeter(num, num2):
#         return F"Rectangle perimeter: {(num + num2) * 2}"
#
#     if isinstance(num, int) and isinstance(num2, int):
#         return F"{area(num, num2)}\n{perimeter(num, num2)}"
#
#     else:
#         return "Enter valid values!"
#
#
# print(rectangle(2, 10))
#


def rectangle(num, num2):
    def area(num, num2):
        return num * num2

    def perimeter(num, num2):
        return (num + num2) * 2

    if isinstance(num, int) and isinstance(num2, int):
        return F'''Rectangle area: {area(num, num2)}
Rectangle perimeter: {perimeter(num, num2)}'''

    else:
        return "Enter valid values!"


print(rectangle(2, 10))

