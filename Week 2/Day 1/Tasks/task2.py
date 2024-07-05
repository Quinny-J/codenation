#
# Task 2
# Create a var called num and check if can be div by 3 or 5
num = 10

# Check if the num var has a number that can be divided by 3 or 5
# We need to divide the number and check if it returns 0 then it can be divided if not return message
if num % 3 == 0 or num % 5 == 0:
    print(f"{num} can be divided by 3 or 5")
else:
    print(f"{num} can not be divided by 3 or 5")

