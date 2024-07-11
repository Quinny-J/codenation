# Task 1
# Create a dict with five fav songs using the artist as a key
# also using any method add two new items to it


# Create dic and store our song data
fav_song_dict = {
    "Eminem": "Cleanin' Out My Closet",
    "Greenday": "Boulevard of Broken Dreams",
    "Linkin Park": "In The End",
    "Snow Patrol": "Chasing Cars",
    "DMX": "Ruff Ryders Anthem"
}

# Print the original dict
print(fav_song_dict)

# Lets add two more songs and artist i like
# I can alter a item or add one depending if it already exists
fav_song_dict.update({
    "Lil Uzi Very": "Buy It",
    "Chase & Status": "All Goes Wrong"
})


# Print the updated dict 
print(fav_song_dict)