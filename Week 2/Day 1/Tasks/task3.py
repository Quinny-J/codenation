#
# Task 3
# Create a var called num and check if can be div by 3 or 7
num = 70 # 21 can be divised by both

# Check if the num var has a number that can be divided by 3 or 7
# We need to divide the number and check if it returns 0 then it can be divided if not return message
if num % 3 == 0 and num % 7 == 0:
    print("fizzbuzz")
elif num % 3 == 0: 
    print("fizz")
elif num % 7 == 0:
    print("buzz")
else:
    print(f"{num} can not be divided by 3 or 7")