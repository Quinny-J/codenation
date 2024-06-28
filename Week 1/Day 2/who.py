# Class is being used to store multiple vars in a catagory in this case strings
class statusColors:
    OKCYAN = '\033[96m' # Python likes ANSI :)
    WARN = '\033[91m'
    WHITE = '\033[0m'

# Class is being used to store multiple vars in a catagory in this case fstrings
class statusMsg:
    UI = f'\033[0m[{statusColors.OKCYAN}UI{statusColors.WHITE}]'
    OK = f'\033[0m[{statusColors.OKCYAN}OK{statusColors.WHITE}]'
    WARN = f'\033[0m[{statusColors.WARN}WARN{statusColors.WHITE}]'

# Class is being used to store multiple vars in a catagory in this case fstrings
class userInfo:
    my_name = input(f"{statusMsg.UI} Please enter your name: ") # "Josh"
    my_age = input(f"{statusMsg.UI} Please enter your age: ") # "21"
    my_color = input(f"{statusMsg.UI} Please enter your fav color: ") # "cyan"

# using fstrings put the var inside {}
if userInfo.my_age.isnumeric():
    print(f"{statusMsg.OK} Hello, {userInfo.my_name} you are {userInfo.my_age} Years old and your fav color is {userInfo.my_color}")
else:
    print(f"{statusMsg.WARN} Please suppy an actual number")

# Check user input and deal with it
#if student == "y":
#    print("You are currently studying")
#else:
#    print("You are not currently studying")
