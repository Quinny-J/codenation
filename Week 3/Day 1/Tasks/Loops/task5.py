# Loops/Task 5
# Write a program that uses a for loop return the multiplication table of the number entered by a user

# Create a var for user input and make sure its a integer
number = int(input("Enter a number for the multiplication table: "))

# Loop through ten times and times the number the user gave by i 1-10
for i in range(1, 11):
    print(f"| {number} | x | {i} | = {number * i} |")
