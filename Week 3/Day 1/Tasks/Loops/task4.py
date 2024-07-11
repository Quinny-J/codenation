# Loops/Task 4
# Write a program that uses a for loop to count vowels in a string input by the user

# string input by the user
user_string = input("Enter a string: ")
# Store our vowels
vowels = 'aeiou'
# Create a var to keep count
count = 0

# Loop through each char of the string the user supplied and count the vowels
# Also the the user string and make it lowercase
for char in user_string.lower():
    if char in vowels:
        count += 1

# Print output
print("Number of vowels in the string:", count)
