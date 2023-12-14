# def kwargs_length(**kwargs):
#     return  len(kwargs)
#
#
# dictionary = {'name': 'Peter', 'age': 25}
#
# dictionary = {}
#
# print(kwargs_length(**dictionary))



def kwargs_length(**dictionary):
    return len(dictionary)


dictionary = {'name': 'Peter', 'age': 25}

dictionary = {}

print(kwargs_length(**dictionary))