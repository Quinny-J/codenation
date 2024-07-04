
# There version
# music = "classical"

# if music == "classical":
#     print("Oh no, Old people music")
# elif music == "no music":
#     print("No music taste")
# else:
#     print("Turn it up!")

# My version     

# # Make a class to store vars and functions  
# class music_data:
#     # Class's variables
#     music_genre = ["classical", "rock", "punk", "dnb"] # Store a few music genre's in a list
#     music_genre_description = ["Oh no, Old people music", "Rock n Roll man!", "You too punky man", "Big dirty stinkin base", "No music taste"]

#     # 
#     def mixer():
#         # Grab the users genre from there input
#         music = input("What music genre are you listing to ? ");

#         # Var to store our count when counting through the list
#         z = 0
#         # i is the differnt music genres
#         # Using for loop to check against each one
#         for i in music_data.music_genre:
#             # 
#             z += 1
#             print(z)
#             # Check if user input is the genre list andd retun description based of count
#             if i == music:
#                 print(music_data.music_genre_description[int(z - 1)])
#             else:
#                 print("no")


#         # Check if there input is in our genre list
#         # if music == music_data.music_genre[0]: # classical is first in our list
#         #     print("Oh no, Old people music")
#         # elif music == music_data.music_genre[1]: # rock is 2nd in our list
#         #     print("Rock n Roll man!")
#         # elif music == music_data.music_genre[2]: # punk is 3rd in our list
#         #     print("You too punky man")
#         # elif music == music_data.music_genre[3]: # dnb is 4th in our list
#         #     print("Big dirty stinkin base")
#         # elif music == "no music":
#         #     print("No music taste")
#         # else:
#         #     print("Turn it up!")

# music_data.mixer();

# # > Greater than
# # < Less than

# temperature = 80

# if temperature > 99:
#     print("Its boiling")
# elif temperature > 90:
#     print ("Its too hot")
# elif temperature > 70:
#     print ("Its warm")
# elif temperature > 40:
#     print ("Its just right")
# else:
#     print("Its a bit chilly")


# place = "Manchester"
# weather = "Sunny"

# if place == "Manchester" and weather == "Sunny":
#     print("Check again")
# elif place == "Manchester" and weather == "Rain":
#     print("Obvs")
# else:
#     print("What? it isn't raining")


day = "Saturday"

if day == "Saturaday" or day == "Sunday":
    print("Its the weekend")
else:
    print('Its not the weekend')