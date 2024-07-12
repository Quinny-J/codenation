# list = [1, 2, 3]
# print(list.Lower())

# print(len("ffff"))

# Define our function to take names

# def name(fname, lname):
#     if len(fname) == 0 or len(lname) == 0:
#         return("Please enter a first name and last name")
#     else:
#         return(f"Welcome , {fname} {lname}")

# fnInput = input("Please Enter your First Name > ").strip().capitalize()
# lnInput = input("Please Enter your Last Name > ").strip().capitalize()

# print(name(fnInput, lnInput))

# fnlnInput = input("Please enter your first and last name : ").strip().split(" ")

# print(f"{fnlnInput[0]} {fnlnInput[1]}")

# def take_order(size, type_of_drink):
#     print(f"I'd like a {size} {type_of_drink} please")

# take_order("Tall", "Latte")
# take_order( "Medium", "Hot Chocolate")

# def prepare_pizza(topping1, topping2, size):
#     print(f"Thanks for ordering a {size} pizza with {topping1} and {topping2}. Enjoy!")

# prepare_pizza("pepperoni", "mushrooms", "large")
# prepare_pizza("cheese", "ham", "medium")

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
    # create a var for our user input
    user_pin = input("Enter your PIN: ")
    # Check if user_pin exists in our bank dict
    if user_pin in bank_data:
        amount = float(input("Enter the amount you would like to withdraw: "))
        # Now check if the account has enough money
        check_balance(user_pin, amount)
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
