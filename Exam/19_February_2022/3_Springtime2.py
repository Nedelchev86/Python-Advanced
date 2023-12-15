def start_spring(**kwargs):
    object_dict = {}
    for key, value in kwargs.items():
        object_dict[value] = object_dict.get(value, [])
        object_dict[value].append(key)

    sorted_object = sorted(object_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for key, value in sorted_object:
        result.append(f"{key}:")
        for el in sorted(value):
            result.append(f"-{el}")

    return "\n".join(result)


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))