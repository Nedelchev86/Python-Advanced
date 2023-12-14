
def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    res = ''
    for name, value in sorted_cheeses:
        sorted_value = sorted(value, reverse=True)
        res += '\n'+name + '\n' + '\n'.join(str(x) for x in sorted_value)
    return res[1:]













print(
 sorting_cheeses(
 Parmesan=[102, 120, 135],
 Camembert=[100, 100, 105, 500, 430],
 Mozzarella=[50, 125],
 )
)
