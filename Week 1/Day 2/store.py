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
my_val1 = int(input("How many apples would you like to buy: ")) # "2"
total = doAppleCost(my_val1, apple_price)

# Print out the response the function gave us
print(f"Total Cost : {total:.2f}")