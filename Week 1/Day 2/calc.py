# + Addition
# - Subtraction
# * Multiply
# / Division
# ** IDK Decimal ?
# % Percentage

# Class is being used to store multiple vars in a category
# You could also maybe use a dictionary instead
class statusColors:
    OKCYAN = '\033[96m' # Python likes ANSI :)
    WARN = '\033[91m'
    WHITE = '\033[0m'

class statusMsg:
    UI = f'\033[0m[{statusColors.OKCYAN}UI{statusColors.WHITE}]'
    OK = f'\033[0m[{statusColors.OKCYAN}OK{statusColors.WHITE}]'
    WARN = f'\033[0m[{statusColors.WARN}WARN{statusColors.WHITE}]'

# Define some methods that the calc uses
methods = ["sub", "mult", "div", "add", "perc", "dec"]

# calculate(val1, cal2, method)
def calculate(val1, val2, method):
    # check if we have the method requested#
    
    if method in methods:
        if method == "mult":
            showStatement = f"{val1} * {val2} = " + str(int(val1) * int(val2)) 
           # print(showStatement)
            return int(val1) * int(val2)
        elif method == "sub":
            showStatement = f"{val1} - {val2} = " + str(int(val1) - int(val2)) 
            #print(showStatement)
            return int(val1) - int(val2)
        elif method == "add":
            showStatement = f"{val1} + {val2} = " + str(int(val1) + int(val2)) 
            #print(showStatement)
            return int(val1) + int(val2)
        elif method == "div":
            showStatement = f"{val1} / {val2} = " + str(int(val1) / int(val2)) 
            #print(showStatement)
            return int(val1) / int(val2)
        elif method == "perc":
            showStatement = f"{val1} % {val2} = " + str(int(val1) % int(val2)) 
            #print(showStatement)
            return int(val1) % int(val2)
        elif method == "dec":
            showStatement = f"{val1} ** {val2} = " + str(int(val1) ** int(val2)) 
            #print(showStatement)
            return int(val1) ** int(val2)
        else:
            return f"{statusMsg.WARN} Please supply a valid method"

# Take user input and assign variables
my_val1 = input(f"{statusMsg.UI} Number 1: ") # "2"
my_method = input(f"{statusMsg.UI} Method (sub/mult/div/add/perc/dec): ") # "mult"
my_val2 = input(f"{statusMsg.UI} Number 2: ") # "2"

if my_val1.isnumeric() & my_val2.isnumeric():
    print(f"{statusMsg.OK} Your result is : {calculate(my_val1, my_val2, my_method)}") # Print out the response the function gave us
else:
    print(f"{statusMsg.WARN} Please supply a valid number") # Print out an error for invalid number
