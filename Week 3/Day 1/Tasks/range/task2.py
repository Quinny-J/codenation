# Range/Task 2
# Write a program that uses a range loop to print even numbers between 1 and 20

# i = 0 at this point then will go up one by one so it loops 20 times
for i in range(1, 21):
    # Check if the number can be divided by 0 if so its an even number
    if i % 2 == 0:
        # Print output
        print(i)