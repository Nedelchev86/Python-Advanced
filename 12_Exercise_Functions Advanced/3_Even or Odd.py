def even_odd(*args):
    parity = 0 if args[-1] == "even" else 1
    result = []

    for i in range(len(args) -1):
        number = args[i]
        if number % 2 == parity:
            result.append(number)
    return result

#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))




def even_odd(*args):
    if args[-1] == "even":
        return list([x for x in args[:-1] if x % 2 == 0])
    else:
        return list([x for x in args[:-1] if x % 2 != 0])



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))