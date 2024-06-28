# + Addition
# - Subtraction
# * Multiply
# / Division
# ** IDK Decimal ?
# % Percentage

# calculate(val1, cal2, method)
def doAppleCost(val1, appleprice):
  doMath = appleprice * val1
  return doMath

# Take user input and assign variables
apple_price = 0.25
apple_limit = False
apple_limit_count = 100

# Parse string input into int
my_val1 = int(input(f"({apple_price}p per apple)How many apples would you like to buy: ")) # "2"

if my_val1>apple_limit_count:
  print(f"We only have {apple_limit_count} left. Please select a reasonable amount")
else:
  # Calculate the cost of x amount of apples
  total = doAppleCost(my_val1, apple_price)
  # Print out the response the function gave us
  print(f"Total Cost : £{total:.2f}")
