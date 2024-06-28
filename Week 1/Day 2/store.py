# Variables
apple_price = 0.25
apple_limit = True
apple_limit_count = 100

# doAppleCost(val1, appleprice)
def doAppleCost(val1, appleprice):
  doMath = appleprice * val1 # 0.25 x 1 for example using * for the times operator
  return doMath # return the doMath variable. 

if apple_limit: # If True we have a limit of 100
  apple_limit_count = 100
  #print(apple_limit_count) # Debuging purpose
else: # If False we don't have a limit per say
  apple_limit_count = 1337
  #print(apple_limit_count)# Debuging purpose

# Parse string input into int
my_val1 = int(input(f"({apple_price}p per apple)How many apples would you like to buy: ")) # "2"

if my_val1>apple_limit_count:
  print(f"We only have {apple_limit_count} left. Please select a reasonable amount")
else:
  # Calculate the cost of x amount of apples
  total = doAppleCost(my_val1, apple_price)
  # Print out the response the function gave us
  print(f"Total Cost : £{total:.2f}") # .2f will give us two decimal places which will turn £2.5 into £2.50 which is the correct way to display currency
