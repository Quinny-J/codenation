# Task
# check if someone is under 18 and return response

# Make a class to store vars and functions  
class order_data:
    # Class's variables
    order_type = ["food", "pop", "alchol"] # Store a few order types's in a list
    order_respnse = ["You can order food", "You can order pop", "Please select something we serve", "You are too young"] # Store a few order response's in a list
    min_age = 18

    def do_age_loc_check():
        # Grab the users genre from there input
        loc = input("Please enter your country ? ")
        # Check the users location from input
        if loc == "UK":
            # Since UKs alchol law is 18 we set that as a min age
            order_data.min_age = 18
            # Take the users age and run a check
            age = int(input("Please enter your age ? "))
            if age >=  order_data.min_age:
                print("You can buy alchol")
            else:
                print(order_data.order_respnse[-1]) # Return the last line which i know is under 18
        else:
            # Default min age if not in uk will be 21 for now
            order_data.min_age = 21


    def do_order():
        # Grab the users genre from there input
        order_input = input("Hello what would you like to order (food/pop/alchol) ? ");

        # Var to store our count when counting through the list
        z = 0
        # i is the differnt music genres
        # Using for loop to check against each one
        for i in order_data.order_type:
            z += 1
            # print(z) # Debugging purpose
            # Check if user input is the genre list andd retun description based of count
            if i == order_input:
                # I'm checking for the 3rd item wich would be the alchol
                if z == 3 and i == order_data.order_type[2]:
                    # Call age check func
                    order_data.do_age_loc_check()
                else:
                    print(order_data.order_respnse[int(z - 1)])
            else:
                print(order_data.order_respnse[-1]) # Return the last line which i know is under 18

order_data.do_order();