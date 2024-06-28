# Take user input and assign it a variable
my_name = input("Please enter your name: ") # "Josh"
my_age = input("Please enter your age: ") # "21"
my_color = input("Please enter your fav color: ") # "cyan"
#student = input("Are you a student Y/N: ".lower()) # "Y"

# Crazy magic
# fstrings can include expresions in curly brackets
#print(f"Hello, {my_name}")
#print(f"You are {my_age} Years old")

# another way of doing it
#print("Hello, " + my_name)
#print("You are " + my_age + " Years old")

# Method 1 using fstrings put the var inside {}
if my_age.isnumeric():
    print(f"Hello, {my_name} you are {my_age} Years old and your fav color is {my_color}")
else:
    print("Please suppy an actual number")

# Check user input and deal with it
#if student == "y":
#    print("You are currently studying")
#else:
#    print("You are not currently studying")
