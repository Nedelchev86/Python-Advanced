
def add_songs(*args):
    song_with_lyrics = {}

    for song, lyrics in args:
        if song not in song_with_lyrics:
            song_with_lyrics[song] = lyrics
        else:
            song_with_lyrics[song].extend(lyrics)
    result = []
    for key, value in song_with_lyrics.items():
        result.append("- " + key)
        result.extend(value)
    return "\n".join(result)


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))