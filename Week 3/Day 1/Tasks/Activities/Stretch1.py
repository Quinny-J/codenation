# Activities/Stretch 1
# Write a program that uses a for loop to print hello world 13 times.
# Then convert it to a while loop that does the same job

def main():
    # Create a empty list to store the numbers
    numbers = []

    # Loop forever and constantly ask for a user input
    while True:
        # Create Input var
        user_input = input("Enter a number (or type 'quit' to finish): ")
        
        # If the user types quit the program will break out of the loop
        if user_input.lower() == 'quit':
            break
        
        try:
            # Convert the user_input to a integer 
            number = int(user_input)
            # Add the number to our list
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")

    # Once loop breaks out it will go here and check if the numbers var has any 
    if numbers:
        # Calculate the sum of the numbers
        total_sum = sum(numbers)
        # Calculate the average of numbers
        average = total_sum / len(numbers)
        
        # Print everything to console
        print("\nNumbers entered:", numbers)
        print("Sum of numbers:", total_sum)
        print("Average of numbers:", average)
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
