# Task
# Ask someone there music taste and return a preset response based upon the genre


# Make a class to store vars and functions  
class music_data:
    # Class's variables
    music_genre = ["classical", "rock", "punk", "dnb"] # Store a few music genre's in a list
    music_genre_description = ["Oh no, Old people music", "Rock n Roll man!", "You too punky man", "Big dirty stinkin base", "No music taste"]

    # 
    def mixer():
        # Grab the users genre from there input
        music = input("What music genre are you listing to ? ");

        # Var to store our count when counting through the list
        z = 0
        # i is the differnt music genres
        # Using for loop to check against each one
        for i in music_data.music_genre:
            # You can do this differently it worked for me in c++ sort of:)
            z += 1
            # print(z) # Debugging purpose
            # Check if user input is the genre list andd retun description based of count
            if i == music:
                print(music_data.music_genre_description[int(z - 1)])
            else:
                print(music_data.music_genre_description[-1]) # Return the last line which i know is no music taste

music_data.mixer();