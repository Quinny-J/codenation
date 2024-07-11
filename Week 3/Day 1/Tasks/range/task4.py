# Range/Task 4
# Write a program that uses a for range loop to calculate all even numbers from 1 - 50

# Create a var to add all the numbers to
sum_numbers = 0

# i = 0 at this point then will go up one by one so it loops 50 times with increments of i
# for i in range(2, 51):
#     # Add the current i number we are on to our sum_numbers var
#     sum_numbers += i

# i = 0 at this point then will go up one by one so it loops 50 times with increments of 2
for i in range(2, 51, 2):
    # Add the current i number we are on to our sum_numbers var
    sum_numbers += i

#Print result
print("Sum of numbers from 1 to 50 is:", sum_numbers)
