# Define some methods that the calc uses
methods = ["sub", "mult", "div", "add", "perc"]

# calculate(val1, cal2, method)
def calculate(val1, val2, method):
    # check if we have the method requested
    if method in methods:
        if method == "mult":
            return int(val1) * int(val2)
        elif method == "sub":
            return int(val1) - int(val2)
        elif method == "add":
            return int(val1) + int(val2)
        elif method == "div":
            return int(val1) / int(val2)
        elif method == "perc":
            return int(val1) % int(val2)
        else:
            return "Method not found"

# Take user input and assign variables
my_val1 = input("Number 1: ") # "2"
my_method = input("Method (sub/mult/div/add/perc): ") # "mult"
my_val2 = input("Number 2: ") # "2"

# Print out the response the function gave us
print("Your result is : " + calculate(my_val1, my_val2, my_method))