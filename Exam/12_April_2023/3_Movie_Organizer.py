def movie_organizer(*args):
    movie_dict = {}
    for name, genre in args:
        if genre not in movie_dict:
            movie_dict[genre] = []
        movie_dict[genre].append(name)
    result = []

    sotred_movies = dict(sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0]) ))

    for key, value in sotred_movies.items():
        result.append(f'{key} - {len(value)}')
        for el in sorted(value):
            result.append("* " + el)
    return "\n".join(result)





print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))