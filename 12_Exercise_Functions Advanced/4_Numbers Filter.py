def even_odd_filter(**kwargs):

    new_dict = dict()
    for key, value in kwargs.items():
        if key == "odd":
            new_dict[key] = [x for x in value if x % 2 != 0]
        else:
            new_dict[key] = [x for x in value if x % 2 == 0]

    return dict(sorted(new_dict.items(), key=lambda x: -len(x[1])))




def even_odd_filter(**kwargs):
    result = dict()
    for key, value in kwargs.items():
        parity = 0 if key == 'even' else 1
        filtres = [x for x in value if x % 2 == parity]
        result[key] = filtres
    return dict(sorted(result.items(), key=lambda x: -len(x[1])))






print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
