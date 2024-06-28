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

# Class is being used to store multiple vars in a catagory in this case booleans and ints
class appleStore:
   apple_price = 0.25
   apple_limit = True
   apple_limit_count = 100


# doAppleCost(val1, appleStore.appleprice)
def doAppleCost(val1, appleprice):
  doMath = appleprice * val1 # 0.25 x 1 for example using * for the times operator
  #print(appleprice) # Debugging
  return doMath # return the doMath variable. 

if appleStore.apple_limit: # If True we have a limit of 100
  appleStore.apple_limit_count = 100
  #print(apple_limit_count) # Debuging purpose
else: # If False we don't have a limit per say
  appleStore.apple_limit_count = 1337
  #print(apple_limit_count)# Debuging purpose

# Parse string input into int
my_val1 = int(input(f"{statusMsg.UI}({appleStore.apple_price}p per apple)How many apples would you like to buy: ")) # "2"

if my_val1>appleStore.apple_limit_count:
  print(f"{statusMsg.WARN} We only have {appleStore.apple_limit_count} left. Please select a reasonable amount")
else:
  # Calculate the cost of x amount of apples
  total = doAppleCost(my_val1, appleStore.apple_price)
  # Print out the response the function gave us
  print(f"{statusMsg.OK} Total Cost : £{total:.2f}") # .2f will give us two decimal places which will turn £2.5 into £2.50 which is the correct way to display currency
