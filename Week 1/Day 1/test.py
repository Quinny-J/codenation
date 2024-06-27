#
# Random Module - https://docs.python.org/3/library/random.html
#

#Imports
import random

# Print some text to console
print("Hello World!")

print("1 | Print your supplied output")
print("2 | Print a random number")

# option will get assigned whatever the user types
option = input("Option (1/2): ")

# Check if the user has typed either 1 or 2
if option == "1":
        arg1 = input("Please enter your desired output: ")
        print(arg1)
elif option == "2":
        print(random.randint(0, 100))
else: # If the user has typed something different return a error msg
        print("Invalid option. Please choose 1 or 2.")
    