# Loops/Task 2
# Write a program that uses a for loop to print even numbers between 1 and 20

# i = 20 at this point so it loops twenty times
for i in range(1, 21):
    # Check if the number can be divided by 0 if so its an even number
    if i % 2 == 0:
        # Print output
        print(i)