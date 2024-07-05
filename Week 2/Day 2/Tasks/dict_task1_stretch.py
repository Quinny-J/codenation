# Task 1 Stretch
# Use a for loop to print my song dict


# Create dic and store our song data
fav_song_dict = {
    "Eminem": "Cleanin' Out My Closet",
    "Greenday": "Boulevard of Broken Dreams",
    "Linkin Park": "In The End",
    "Snow Patrol": "Chasing Cars",
    "DMX": "Ruff Ryders Anthem"
}

for artist, song in fav_song_dict.items():
    print(f"I like {song} by {artist}")