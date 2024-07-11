# Loops/Task 3
# Write a program that uses a for loop to calculate all number from 1 - 100

# Create a var to add all the numbers to
sum_numbers = 0

# i = 100 at this point so it loops 100 times
for i in range(1, 101):
    # Add the current i number we are on to our sum_numbers var
    sum_numbers += i

#Print result
print("Sum of numbers from 1 to 100 is:", sum_numbers)
