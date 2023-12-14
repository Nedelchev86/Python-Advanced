def grocery_store(**kwargs):
    result = []
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for key, value in sorted_dict.items():
        result.append(F"{key}: {value}")
    return "\n".join(result)


# def grocery_store(**kwargs):
#     sorted_Result = [F"{key}: {value}" for key, value  in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
#     return "\n".join(sorted_Result)

def grocery_store(**kwargs):
    return "\n".join([F"{key}: {value}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))])



print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
