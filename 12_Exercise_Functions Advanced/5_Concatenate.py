def concatenate(*args, **kvargs):
    result = "".join(args)
    for key, value in kvargs.items():
        result = result.replace(key, value)
    return result










print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
