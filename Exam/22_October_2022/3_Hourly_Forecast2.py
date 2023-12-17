def forecast(*args):
    filtres_list = [x for x in sorted(args, key=lambda x: (x[1][0] == "R", x[1][0] == "C", x[0]))]
    my_list = [F"{x[0]} - {x[1]}" for x in filtres_list]
    return "\n".join(my_list)

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))