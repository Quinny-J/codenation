# Activities/Task 2
# Write a program that uses a for nested loop to print out the multiplication tables from 1 to 12
# Also include a line-break between each table

# i = 0 at this point then will go up one by one so it loops 13 times
for i in range(1, 13):
    # Print the current number i is on through the range
    print(f"Multiplication table for {i}:")
    # n = 0 at this point then will go up one by one so it loops 13 times
    for n in range(1, 13):
        # Print the current number i and the multiplication table and then times them together 
        print(f"{i} x {n} = {i * n}")
    print()  # Print a line break after each table