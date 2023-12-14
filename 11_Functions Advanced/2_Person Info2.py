# def get_info(**kwargs):
#     return F"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"
#
#
#
# print(get_info(**{"name": "George", "town":
# "Sofia", "age": 20}))



def get_info(name, town, age):
    return F"This is {name} from {town} and he is {age} years old"

