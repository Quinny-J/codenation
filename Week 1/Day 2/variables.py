# All Around The World - Print the 8th character
#print("All Around The World"[7].upper()) # Print the 8th char in uppercase. Always starts at 0 not 1 :)

# Use and print a var
# if your lazy make a var of a var instead of renaming  | mn = my_name not good practise at all 
#my_name = "Josh"
#print("Hello, " + my_name)

# Take user input and assign it a variable
my_name = input("Please enter your name: ") # "Josh"
my_age = input("Please enter your age: ") # "21"
student = input("Are you a student Y/N: ".lower()) # "Y"

# Crazy magic
# fstrings can include expresions in curly brackets
#print(f"Hello, {my_name}")
#print(f"You are {my_age} Years old")

# another way of doing it
#print("Hello, " + my_name)
#print("You are " + my_age + " Years old")

# Method 1 using fstrings put the var inside {}
print(f"Hello, {my_name} you are {my_age} Years old")
# Method 2
#print("Hello, " + my_name + " you are " + my_age + " Years old")
# Method 3 - Many easier ways to do this
#print("Hello, {} you are {} Years old".format(my_name, my_age))

# Check user input and deal with it
if student == "y":
    print("You are currently studying")
else:
    print("You are not currently studying")

# + Addition
# - Subtraction
# * Multiply
# / Division
# **
# %
methods = ["sub", "mult", "div", "add"]

def calculate(val1, val2, method):
    if method in methods:
        if method == "mult":
            return int(val1) * int(val2)
        elif method == "sub":
            return int(val1) - int(val2)
        elif method == "add":
            return int(val1) + int(val2)
        elif method == "div":
            return int(val1) / int(val2)
        else:
            return "Method not found"

my_val1 = input("Number 1: ") # "2"
my_method = input("Method (sub/mult/div/add): ") # "mult"
my_val2 = input("Number 2: ") # "2"

print(calculate(my_val1, my_val2, my_method))
    