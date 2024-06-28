# + Addition
# - Subtraction
# * Multiply
# / Division
# ** IDK Decimal ?
# % Percentage

# Define some methods that the calc uses
methods = ["sub", "mult", "div", "add", "perc", "dec"]

# calculate(val1, cal2, method)
def calculate(val1, val2, method):
    # check if we have the method requested
    if method in methods:
        if method == "mult":
            showStatement = f"{val1} * {val2} = " + str(int(val1) * int(val2)) 
            print(showStatement)
            return int(val1) * int(val2)
        elif method == "sub":
            showStatement = f"{val1} - {val2} = " + str(int(val1) - int(val2)) 
            print(showStatement)
            return int(val1) - int(val2)
        elif method == "add":
            showStatement = f"{val1} + {val2} = " + str(int(val1) + int(val2)) 
            print(showStatement)
            return int(val1) + int(val2)
        elif method == "div":
            showStatement = f"{val1} / {val2} = " + str(int(val1) / int(val2)) 
            print(showStatement)
            return int(val1) / int(val2)
        elif method == "perc":
            showStatement = f"{val1} % {val2} = " + str(int(val1) % int(val2)) 
            print(showStatement)
            return int(val1) % int(val2)
        elif method == "dec":
            showStatement = f"{val1} ** {val2} = " + str(int(val1) ** int(val2)) 
            print(showStatement)
            return int(val1) ** int(val2)
        else:
            return "Method not found"

# Take user input and assign variables
my_val1 = input("Number 1: ") # "2"
my_method = input("Method (sub/mult/div/add/perc/dec): ") # "mult"
my_val2 = input("Number 2: ") # "2"

# Print out the response the function gave us
print(f"Your result is : {calculate(my_val1, my_val2, my_method)}")
