# EXTRA
# Write a programme to dispense cash to a user
# withdrawal(), check_balance(), dispense()

# Create a dictionary to store the pin and balance 
bank_data = {
    "1234": {"balance": 1000},
    "5678": {"balance": 500}
}

# Create our withdraw function
def withdrawal():
    # Keep it in a loop until the user has entered a valid pin
    while True:
        # create a var for our user input
        user_pin = input("Enter your PIN: ")
        # Check if user_pin exists in our bank dict
        if user_pin in bank_data:
            amount = float(input("Enter the amount you would like to withdraw: "))
            # Now check if the account has enough money
            check_balance(user_pin, amount)
            break
        else:
            # If the user_pin is invalid print to console
            print("Invalid PIN. Please try again.")

# Create our check balance function
def check_balance(pin, amount):
    # Create a var to for the bank details
    balance = bank_data[pin]["balance"]
    # check if the bank details contain the correct amount of money
    if amount <= balance:
        # if so send our data to the dispense function
        dispense(pin, amount)
    else:
        # if they don't have enough money
        print("Sorry, insufficient funds.")

# Create our dispense function
def dispense(pin, amount):
    # Subtract the amount of money we are dispensing from the bank
    bank_data[pin]["balance"] -= amount
    # Print our new balance and tell the user to wait for there cash
    print(f"Your new balance is £{bank_data[pin]['balance']:.2f}. \nPlease wait while we dispense £{amount:.2f}. ")

# Run the withdrawal function 
withdrawal()