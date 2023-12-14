# def age_assignment(*args, **kwargs):
#     result = []
#     for name in args:
#         result.append((F"{name} is {kwargs[name[0]]} years old."))
#
#     return  "\n".join(sorted(result))


# def age_assignment(*args, **kwargs):
#     result = {}
#     for name in args:
#         first_letter = name[0]
#         age = kwargs[first_letter]
#         result[name] = age
#     return "\n".join([F"{key} is {value} years old." for key, value in sorted(result.items(), key=lambda x: x[0])])


def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        result[name] = age
    sorted_dict = [F"{key} is {value} years old." for key, value in sorted(result.items(), key=lambda x: x[0])]
    return "\n".join(sorted_dict)



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment2("Amy", "Bill", "Willy", W=36, A=22, B=61))
