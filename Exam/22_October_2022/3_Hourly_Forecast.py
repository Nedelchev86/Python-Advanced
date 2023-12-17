def forecast(*args):
    final_dict = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }
    for location, weather in args:
        final_dict[weather].append(location)
    result = []

    for key, value in final_dict.items():
        for v in sorted(value):
            result.append(f"{v} - {key}")
    return "\n".join(result)

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))